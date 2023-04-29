import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QListView, QTableView, QHBoxLayout, QWidget
from PySide6.QtCore import Qt
from PySide6.QtGui import QStandardItemModel, QStandardItem
from sqlalchemy import text, create_engine
from sqlalchemy.orm import sessionmaker

#Create a SQLAlchemy engine and session
engine = create_engine('sqlite:///Y:/Masterarbeit/Skripte/Sample Viewer/components/samples.db')
Session = sessionmaker(bind=engine)
session = Session()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set up the UI
        self.setWindowTitle("Table Viewer")
        self.resize(800, 600)

        # Create a QListView to display the tables
        self.table_list = QListView()
        self.table_list.setEditTriggers(QListView.NoEditTriggers)
        self.table_list.setSelectionMode(QListView.SingleSelection)
        self.table_list.setModel(self.get_table_list())

        # Create a QTableView to display the data
        self.table_view = QTableView()

        # Add the widgets to a layout
        layout = QHBoxLayout()
        layout.addWidget(self.table_list)
        layout.addWidget(self.table_view)

        # Create a central widget to hold the layout
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Connect the table selection to the table view
        self.table_list.selectionModel().selectionChanged.connect(self.display_table)

    def get_table_list(self):
        # Get a list of the tables in the database
        tables = session.execute(text("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name")).fetchall()
        table_list = [table[0] for table in tables]

        # Create a model to display the tables in the QListView
        model = QStandardItemModel()
        for table in table_list:
            item = QStandardItem(table)
            model.appendRow(item)

        return model

    def display_table(self, selected, deselected):
        # Get the selected table from the QListView
        index = selected.indexes()[0]
        table_name = index.data(Qt.DisplayRole)

        # Get the data from the table
        data = session.execute(text(f"SELECT * FROM {table_name}")).fetchall()

        # Get the column names from the table
        column_names = session.execute(text(f"PRAGMA table_info({table_name})")).fetchall()
        column_names = [col[1] for col in column_names]

        # Create a model to display the data in the QTableView
        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(column_names)
        for n_row, row in enumerate(data):
            for n_col, value in enumerate(row):
                item = QStandardItem(str(value))
                model.setItem(n_row, n_col, item)

        self.table_view.setModel(model)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())