import sys
import re
import os
import numpy as np 
import components.ReadCryoScan as ReadCryoScan
from PySide6 import QtWidgets, QtSql
from PySide6.QtCore import Qt, QStringListModel
from PySide6.QtWidgets import QApplication, QMainWindow, QListView, QFileDialog, QHeaderView,QTableWidgetItem
from PySide6.QtGui import QPixmap, QStandardItemModel, QStandardItem
from PySide6.QtSql import QSqlDatabase, QSqlTableModel
from components.mainwindow_ui import Ui_MainWindow
from components.filemanager import ImageTypeDialog, DragAndDropBox
from components.image_tools import *
from components.cropper import *
from sqlalchemy import create_engine,text , Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, backref, declarative_base
from components.ORM_Database import *
from components.tc_ppms import * 
from components.xrd_reader import *
import definitive_screening_design as dsd
try:
    from components.helpers import *
except:
    from helpers import *


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # sys.stderr = StdoutRedirector(self.ui.log)
        self.experiment = None 
        self.crop_window = None
        self.current_tab = 0


        self.items = []
        self.ui.add_files.pressed.connect(self.show_drag_and_drop_box)
        self.ui.analyze_color.pressed.connect(self.color_analyzer)
        self.ui.actionImage_Crop_Module.triggered.connect(self.crop)
        self.ui.tabWidget.currentChanged.connect(self.set_current_tab)
        self.ui.show_comparator.triggered.connect(self.compare_images)
        self.ui.dsd_okay_button.clicked.connect(self.add_item)
        self.ui.nFakeFactors.valueChanged.connect(self.gen_dsd)


        search_comboboxes = [self.ui.search_user, self.ui.search_element]
        for combobox in search_comboboxes: combobox.currentIndexChanged.connect(self.filter_results)

        self.connect_db()
        self.display_table("samples", None)
            
    def add_item(self):
            # Get the values from the line edits
            key = self.ui.key_edit.text()
            minimum = self.ui.min_edit.text()
            maximum = self.ui.max_edit.text()

            # Add the values to the table widget
            row_position = self.ui.dsdTable.rowCount()
            self.ui.dsdTable.insertRow(row_position)
            self.ui.dsdTable.setItem(row_position, 0, QTableWidgetItem(key))
            self.ui.dsdTable.setItem(row_position, 1, QTableWidgetItem(minimum))
            self.ui.dsdTable.setItem(row_position, 2, QTableWidgetItem(maximum))

            # Add the key-value pair to the list
            self.items.append((key, minimum, maximum))

            # Clear the line edits
            self.ui.key_edit.clear()
            self.ui.min_edit.clear()
            self.ui.max_edit.clear()
            self.gen_dsd()

    def gen_dsd(self):
        def return_dict(self):
            # Create a dictionary from the list of key-value pairs
            dictionary = {}
            for item in self.items:
                key, minimum, maximum = item
                dictionary[key] = [int(minimum), int(maximum)]

            # Return the dictionary
            # self.close()
            return dictionary
        
        dicti = return_dict(self)
        nfake = self.ui.nFakeFactors.value() 
        # df = dsd.generate(factors_dict=dicti,n_fake_factors=nfake)
        strings = dsd.generate(factors_dict=dicti,n_fake_factors=nfake).to_string()
        self.ui.dsd_result.setText(strings)

    def compare_images(self):
        p1 = r"C:\Users\yassi\OneDrive\Dokumente\GitHub\Masterarbeit\Dokumente\Messdaten\Keyencejpg\YRY1a1_overview.jpg"
        p2 = r"C:\Users\yassi\OneDrive\Dokumente\GitHub\Masterarbeit\Dokumente\Messdaten\Keyencejpg\YRY3n1_overview.jpg"
        analyze_colors([p1,p2])
    #Database related helper functions
    def connect_db(self):
        #Connect Database Widget
        p2 = r"Y:/Masterarbeit/Skripte/SampleViewer/components/samples.db"
        p1 = r"C:\Users\yassi\OneDrive\Dokumente\GitHub\Masterarbeit\Skripte\SampleViewer\components\samples.db"
        self.dbpath = p1 if os.path.exists(p1) else p2
        engine = create_engine(f'sqlite:///{self.dbpath}')
        Session = sessionmaker(bind=engine)
        self.dbsession = Session()
        self.table_list = self.ui.table_selector
        self.table_list.setEditTriggers(QListView.NoEditTriggers)
        self.table_list.setSelectionMode(QListView.SingleSelection)
        self.table_list.setModel(self.get_table_list())
        # Create a QTableView to display the data
        self.table_view = self.ui.db_table
        self.table_view.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table_view.verticalHeader().setVisible(False)
        # Connect the table selection to the table view
        self.table_list.selectionModel().selectionChanged.connect(self.display_table)
        delegate = CenterDelegate()
        self.table_view.setItemDelegate(delegate)
        self.ui.result_list.setModel(self.gen_result_list(self.dbsession.query(Sample_DB).all()))
        self.ui.result_list.setEditTriggers(QListView.NoEditTriggers)
        self.ui.result_list.setSelectionMode(QListView.SingleSelection)
        self.ui.result_list.selectionModel().selectionChanged.connect(self.update_current_sample)
        self.fill_elements()


    def filter_results(self):
        username = self.ui.search_user.currentText()
        element = self.ui.search_element.currentText()

        search_query = "SELECT sample_name FROM samples WHERE "
        search_needed = any([username != "All", element != "All"])
        searched_already = ""
        if username != "All":
            search_query= search_query + f"user_name = '{username}'"
            searched_already = "AND "
        if element != "All":
            search_query= search_query + f"{searched_already}element = '{element}'"


        if search_needed:
            samples = self.dbsession.execute(text(f"{search_query}")).fetchall()
        else:
            samples = self.dbsession.query(Sample_DB).all()

        # samples = self.dbsession.execute(text("SELECT sample_name FROM samples WHERE user_name = :username AND element = :tvalue"),{"username": user, "tvalue": 2}).fetchall()
        
        self.ui.result_list.setModel(self.gen_result_list(samples))
        self.ui.result_list.setEditTriggers(QListView.NoEditTriggers)
        self.ui.result_list.setSelectionMode(QListView.SingleSelection)
        self.ui.result_list.selectionModel().selectionChanged.connect(self.update_current_sample)


    def fill_elements(self):
        samples = self.dbsession.query(Sample_DB).all()
        self.sample_names = [sample.sample_name for sample in samples]
        self.elements = remove_duplicates([sample.element for sample in samples])

        self.users = remove_duplicates([sample.user_name for sample in samples])
        populate_combobox(self.elements, self.ui.search_element)
        populate_combobox(self.users, self.ui.search_user)

    def color_analyzer(self, path=None):
        if path==None:
            print("Analyze colors")
            analyze_colors([self.current_image_path])

    def display_table(self, selected, deselected):
        # Get the selected table from the QListView
        if type(selected) != str:
            index = selected.indexes()[0]
            table_name = index.data(Qt.DisplayRole)
        else:
            table_name = selected

        # Get the data from the table
        data = self.dbsession.execute(text(f"SELECT * FROM {table_name}")).fetchall()

        # Get the column names from the table
        column_names = self.dbsession.execute(text(f"PRAGMA table_info({table_name})")).fetchall()
        column_names = [col[1] for col in column_names]

        # Add a new column called "sample_name" if table_name is not "samples"
        if table_name != "samples":
            column_names.insert(1, "sample_name")

        # Create a model to display the data in the QTableView
        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(column_names)

        for n_row, row in enumerate(data):
            # Add a new column with the sample name if table_name is not "samples"
            if table_name != "samples":
                sample_id = row[0]  # Assuming the id field is the first column
                sample_name = self.dbsession.execute(text(f"SELECT sample_name FROM samples WHERE id = {sample_id}")).fetchone()[0]
                row = list(row)
                row.insert(1, sample_name)

            for n_col, value in enumerate(row):
                item = QStandardItem(str(value))
                model.setItem(n_row, n_col, item)

        self.table_view.setModel(model)
        self.table_view.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table_view.verticalHeader().setVisible(False)
    
    def get_table_list(self):
        # Get a list of the tables in the database
        tables = self.dbsession.execute(text("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name")).fetchall()
        table_list = [table[0] for table in tables]

        # Create a model to display the tables in the QListView
        model = QStandardItemModel()
        for table in table_list:
            item = QStandardItem(table)
            model.appendRow(item)

        return model
    
    def gen_result_list(self, sample_list):
        samples = sample_list
        sample_names = [sample.sample_name for sample in samples]
        model = QStandardItemModel()
        for sample in sample_names:
            item = QStandardItem(sample)
            model.appendRow(item)

        return model
    
    #UI related functions
    def set_current_tab(self):
        self.current_tab = self.ui.tabWidget.currentIndex()
        self.update_view()
    
    def update_current_sample(self, selected, deselected):
        index = selected.indexes()[0]
        sample_name = index.data(Qt.DisplayRole)
        self.selected_name = sample_name
        self.selected_id =  self.dbsession.query(Sample_DB).filter_by(sample_name=self.selected_name).first().id
        self.update_view()
        # print(f"Selected {sample_name} [ID {self.selected_id}]")
        
    def update_view(self):
        tab, id, name = [self.current_tab, self.selected_id, self.selected_name]
        tabname = self.ui.tabWidget.tabText(tab)
        functions = { "Images": {"clear_name": "Images", "function": self.show_image, "bla": "Bla A"},
                    "Tc PPMS": {"clear_name": "Tc PPMS", "function": self.show_ppms, "bla": "Bla B"},
                    "XRD": {"clear_name": "Sample C", "function": self.show_xrd, "bla": "Bla C"},
                    "D": {"clear_name": "Sample D", "function": "Function D", "bla": "Bla D"}
                }
        if tabname in functions: functions[tabname]["function"]()
        # print(tabname)

    def show_image(self):
        #load image
        image =  self.dbsession.query(Picture_DB).filter_by(sample_id=self.selected_id, type="Overview").first()
        self.current_image_path = image.path
        pixmap = QPixmap(self.current_image_path)
        pixmap = pixmap.scaled(self.ui.picture_screen.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.ui.picture_screen.setPixmap(pixmap)
        # self.ui.picture_screen.pi

    def show_ppms(self):
        ppms =  self.dbsession.query(TC_DB).filter_by(sample_id=self.selected_id).first()
        ax = self.ui.plot_tc_ppms.ax
        canvas = self.ui.plot_tc_ppms.canvas
        ax.clear()
        ax.set_xlim(80,100)

        if ppms != None:
            file_path = ppms.file_path
            experiment_data = Tc_PPMS_Data(file_path)
            # line1 = ax.plot(experiment_data.temperature, experiment_data.voltage_mod)
            line2 = ax.plot(experiment_data.temperature, normalize_array(experiment_data.voltage))

        else:

            ax.text(80, 0, 'No PPMS Data Available', style='italic', size=40,  bbox={'facecolor': 'red', 'alpha': 0.5, 'pad': 10})
        ax.set_xlabel('Temperature (K)')
        ax.set_ylabel('Voltage (V)')
        ax.set_title('Voltage vs. Temperature')
        canvas.draw()

    def show_xrd(self):
        xrd =  self.dbsession.query(XRD_DB).filter_by(sample_id=self.selected_id).first()
        ax = self.ui.plot_xrd.ax
        canvas = self.ui.plot_xrd.canvas
        ax.clear()
        if xrd != None:
            file_path = xrd.xrd_file_path
            x, y = read_xrd_data(file_path)
            ax.set_xlim(x.min(), x.max())

            line1 = ax.plot(x, normalize_array(y))
        else:
            ax.text(0, 0, 'No XRD Data Available', style='italic', size=40,  bbox={'facecolor': 'red', 'alpha': 0.5, 'pad': 10})
        ax.set_ylim(0,1)
        ax.set_xlabel('Degrees (°)')
        ax.set_ylabel('Count')
        # ax.set_title('Voltage vs. Temperature')
        canvas.draw()




    def crop(self):

        self.crop_window = crop_module()
        self.crop_window.show()

    def load_db(self):
        self.db.open_db()
        # Abfrage erstellen
        query = QtSql.QSqlQuery(self.db.database)
        query.exec("SELECT * FROM samples")
        # Tabellenmodell erstellen und Daten hinzufügen
        self.table_model = QtSql.QSqlTableModel()
        self.table_model.setTable("samples")
        self.table_model.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)
        self.table_model.select()
        # self.table_model = generate_aliases(self.table_model)

        # TableView-Widget erstellen und Tabellenmodell hinzufügen
        # self.ui.table_database = QtWidgets.QTableView()
        self.ui.table_database.setModel(self.table_model)
        self.ui.table_database.show()
        # Verbindung schließen
        # self.db.database.close()

    def show_drag_and_drop_box(self):
        # Dialog für Drag-and-Drop-Box erstellen und anzeigen
        dialog = DragAndDropBox(parent=self)
        if dialog.exec():
            sample_name, returndata = dialog.get_data()

            self.db.new_sample(sample_name)

            for element in returndata:
                type_of = element[0]
                if type_of == "images":
                    images_list = element[1]
                    rem_images = []
                    keyence_images = []
                    for image in images_list:
                        if image[0].find("SEM") != -1: rem_images.append(image)  
                        if image[0].find("Keyence") != -1: keyence_images.append(image) 
            self.db.set_var(sample_name, "rem_images", "rem_images")
            self.db.set_var(sample_name, "keyence_images", "keyence_images")

            print("reload")
            self.load_db()

    def plot(self):
        pass



if __name__ == "__main__":
    app = QApplication(sys.argv)
    # app.setWindowTitle("Sample Viewer")
    app.setApplicationName("CSD Sample Viewer")
    app.setApplicationDisplayName("CSD Sample Viewer")
    window = MainWindow()
    window.showMaximized()

    sys.exit(app.exec())


