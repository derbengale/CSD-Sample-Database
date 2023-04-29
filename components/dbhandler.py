from PySide6.QtSql import QSqlDatabase, QSqlQuery
from PySide6 import QtCore
import os

def create_db():
    import sqlite3

    # Verbindung zur Datenbank herstellen
    conn = sqlite3.connect('database.db')

    # Ein Cursor-Objekt erstellen
    cursor = conn.cursor()

    # Eine Tabelle erstellen
    cursor.execute('''
        CREATE TABLE samples
        (id INTEGER PRIMARY KEY,
        user TEXT,
        sample_name TEXT,
        element TEXT,
        Tc_PPMS_path TEXT,
        Jc_PPMS_path TEXT,
        xrd_file TEXT,
        rem_images TEXT,
        pyrolysis_batch TEXT,
        pyrolysis_data TEXT,
        pyrolysis_date TEXT,
        crystallization_batch TEXT,
        crystallization_data TEXT,
        crystallization_date TEXT,
        both_batch TEXT,
        both_data TEXT,
        both_date TEXT)
        ''')

    # Die Änderungen bestätigen und die Verbindung schließen
    conn.commit()
    conn.close()

def show_db(db):
    from PySide6 import QtWidgets, QtSql
    import sys

    app = QtWidgets.QApplication(sys.argv)

    # # Verbindung zur Datenbank herstellen
    # db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
    # db.setDatabaseName(r'Y:\Masterarbeit\Skripte\Sample Viewer\components\database.db' if os.path.exists(r'Y:\Masterarbeit\Skripte\Sample Viewer\components\database.db') else r'C:\Users\yassi\OneDrive\Dokumente\GitHub\Masterarbeit\Skripte\Sample Viewer\components\database.db')

    if not db.open():
        print("Cannot establish a database connection")
        exit(1)

    # Abfrage erstellen
    query = QtSql.QSqlQuery()
    query.exec("SELECT * FROM samples")

    # Tabellenmodell erstellen und Daten hinzufügen
    table_model = QtSql.QSqlTableModel()
    table_model.setTable("samples")
    table_model.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)
    table_model.select()

    # TableView-Widget erstellen und Tabellenmodell hinzufügen
    table_view = QtWidgets.QTableView()
    table_view.setModel(table_model)
    table_view.resize(800, 600)
    table_view.show()

    # Verbindung schließen
    db.close()

    sys.exit(app.exec())

def generate_aliases(table_model):
    display_names = {
    "sample_name": "Probenname",
    "Tc_PPMS_path": "Tc PPMS Pfad",
    "Jc_PPMS_path": "Jc PPMS Pfad",
    "xrd_file": "XRD-Datei",
    "rem_images": "REM-Bilder",
    "pyrolysis_batch": "Pyrolyse Batch",
    "pyrolysis_data": "Pyrolyse Daten",
    "pyrolysis_date": "Pyrolyse Datum",
    "crystallization_batch": "Kristallisation Batch",
    "crystallization_data": "Kristallisation Daten",
    "crystallization_date": "Kristallisation Datum",
    "both_batch": "Beides Batch",
    "both_data": "Beides Daten",
    "both_date": "Beides Datum"
    }

    for i in range(table_model.columnCount()):
        field_name = table_model.record().fieldName(i)
        if field_name in display_names:
            table_model.setHeaderData(i, QtCore.Qt.Horizontal, display_names[field_name])
    
    return table_model



class SampleDatabase:
    def __init__(self, database_path):
        self.database_path = database_path
        self.database = QSqlDatabase.addDatabase('QSQLITE')
        self.database.setDatabaseName(database_path)

    def db_connection(func):
        def wrapper(self, *args, **kwargs):
            self.open_db()
            result = func(self, *args, **kwargs)
            self.database.commit()
            self.close_db()

            return result
        return wrapper

    @classmethod
    def show_db(cls, database_path):
        from PySide6 import QtWidgets, QtSql
        import sys

        app = QtWidgets.QApplication(sys.argv)

        # Verbindung zur Datenbank herstellen
        db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName(database_path)

        if not db.open():
            print("Cannot establish a database connection")
            exit(1)

        # Abfrage erstellen
        query = QtSql.QSqlQuery()
        query.exec("SELECT * FROM samples")

        # Tabellenmodell erstellen und Daten hinzufügen
        table_model = QtSql.QSqlTableModel()
        table_model.setTable("samples")
        table_model.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)
        table_model.select()

        # Aliase generieren
        table_model = generate_aliases(table_model)

        # TableView-Widget erstellen und Tabellenmodell hinzufügen
        table_view = QtWidgets.QTableView()
        table_view.setModel(table_model)
        table_view.resize(800, 600)
        table_view.show()

        # Verbindung schließen
        db.close()

        sys.exit(app.exec())

    @db_connection
    def add_column(self, new_key):
        query = QSqlQuery()
        query.exec(f'ALTER TABLE samples ADD COLUMN {new_key} TEXT')

    @db_connection
    def remove_column(self, new_key):

        query = QSqlQuery()
        query.exec(f'ALTER TABLE samples DROP COLUMN {new_key}')

    @db_connection
    def rename_column(self, old_key, new_key):
        query = QSqlQuery()
        query.exec(f'ALTER TABLE samples RENAME COLUMN {old_key} TO {new_key}')
        
    @db_connection
    def set_var(self, sample_name, variable_name, new_value):
        query = QSqlQuery()
        query.exec(f"SELECT * FROM samples WHERE sample_name = {sample_name}")
        if query.next():
            sample_id = query.value(0)
            query.prepare(f"UPDATE samples SET {variable_name} = ? WHERE id = ?")
            query.addBindValue(new_value)
            query.addBindValue(sample_id)
            query.exec()

    @db_connection
    def new_sample(self, sample_name, username="Yassin"):
        if self.exists(sample_name) == None:    
            query = QSqlQuery(self.database)
            query.prepare(f"INSERT INTO samples (sample_name) VALUES (:sample_name)")
            query.bindValue(":sample_name", sample_name)
            query.prepare(f"INSERT INTO samples (user) VALUES (:user)")
            query.bindValue(":sample_name", username)
            query.exec()

    @db_connection
    def delete_sample(self, sample_name):
        query = QSqlQuery()
        query.prepare(f"DELETE FROM samples WHERE sample_name=:sample_name")
        query.bindValue(":sample_name", sample_name)
        query.exec()

    def open_db(self):
        if not self.database.open():
            print("Cannot establish a database connection")
            exit(1)
        else:
            print("opened db")

    @db_connection
    def exists(self,sample_name):
        query = QSqlQuery()
        query.prepare("SELECT id FROM samples WHERE sample_name = :sample_name")
        query.bindValue(":sample_name", sample_name)
        query.exec()
        if query.next():
            sample_id = query.value(0)
            return sample_id
        else:
            return None

    def close_db(self):
        self.database.close()

    @db_connection
    def delete_item_by_id(self, item_id):
        query = QSqlQuery()
        query.prepare(f"DELETE FROM samples WHERE id = :id")
        query.bindValue(":id", item_id)
        if not query.exec():
            print("Error executing query:", query.lastError().text())
        else:
            print(f"Deleted item with ID {item_id} from samples")
        
    @db_connection
    def mass_add_samples(self, comma_seperated_sample_names = [], username="Yassin"):
        for sample_name in comma_seperated_sample_names:
            self.new_sample(username, sample_name)
def fetch_files(directory, file_ending):
    import os
    csw_files = [f for f in os.listdir(directory) if f.endswith(file_ending)]
    return csw_files

if __name__ == "__main__":
    db = SampleDatabase(r'Y:\Masterarbeit\Skripte\Sample Viewer\components\database.db')
    # search_directory = r'C:\Users\yassi\OneDrive\Dokumente\GitHub\Masterarbeit\Dokumente\Messdaten\Jc_self'
    # sample_names = fetch_files(search_directory, '.csw')
    # db.mass_add_samples(sample_names, username="Yassin")

    display_names = {
    "sample_name": "Probenname",
    "Tc_PPMS_path": "Tc PPMS Pfad",
    "Jc_PPMS_path": "Jc PPMS Pfad",
    "xrd_file": "XRD-Datei",
    "rem_images": "REM-Bilder",
    "pyrolysis_batch": "Pyrolyse Batch",
    "pyrolysis_data": "Pyrolyse Daten",
    "pyrolysis_date": "Pyrolyse Datum",
    "crystallization_batch": "Kristallisation Batch",
    "crystallization_data": "Kristallisation Daten",
    "crystallization_date": "Kristallisation Datum",
    "both_batch": "Beides Batch",
    "both_data": "Beides Daten",
    "both_date": "Beides Datum"
    }
    skip=False
    if not skip:
        db.new_sample( "Y1a1", username="Yassin")
        db.set_var("Y1a1", "Tc_PPMS_path", r"Y:\Masterarbeit\Dokumente\Messdaten\Tc_ind\YRY1a1.txt")
        db.set_var("Y1a1", "Jc_PPMS_path", r"Y:\Masterarbeit\Dokumente\Messdaten\Jc_self\YRY1a1.csw")
        db.set_var("Y1a1", "rem_images", r"Y:\Masterarbeit\Dokumente\Messdaten\Keyencejpg\YRY1a1_overview.jpg")
        db.set_var("Y1a1", "pyrolysis_batch", r"Y:\Masterarbeit\Dokumente\Messdaten\CSD\Y1a1\cryst_Y_780_200.xml")
        db.set_var("Y1a1", "pyrolysis_data", r"Y:\Masterarbeit\Dokumente\Messdaten\CSD\Y1a1\Pyro_YR_Test0.txt")
        db.set_var("Y1a1", "crystallization_batch", r"Y:\Masterarbeit\Dokumente\Messdaten\CSD\Y1a1\cryst_Y_780_200.xml")
        db.set_var("Y1a1", "crystallization_data", r"Y:\Masterarbeit\Dokumente\Messdaten\CSD\Y1a1\YR_1_Solutions-Eu,Dy,Gd,Y.txt")
    SampleDatabase.show_db(db.database_path)