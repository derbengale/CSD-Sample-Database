import sys
from PySide6.QtCore import Qt, QMimeData, QSize
from PySide6.QtGui import QDragEnterEvent, QDropEvent, QPixmap
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QListWidget, QListWidgetItem, QLineEdit, QPushButton, QDialog, QHBoxLayout, QComboBox
from PySide6.QtGui import QFont

class ImageTypeDialog(QDialog):
    def __init__(self, file_path, parent=None):
        super().__init__(parent)
        self.file_name = file_path.split("/")[-1]
        self.filepath = file_path

        self.setWindowTitle("Choose Image Type")
        self.filename_label = QLabel(f"{self.file_name}")
        self.image_type_label = QLabel("Select image type:")
        self.image_type_combobox = QComboBox()
        self.image_type_combobox.setEditable(True)
        self.image_type_combobox.addItems(["Keyence (Overview)","Keyence (Panorama)","Keyence (Other Detail)", "SEM (500x)","SEM (1000x)","SEM (2000x)","SEM (5000x)"])
        self.ok_button = QPushButton("Okay")

        layout = QVBoxLayout()
        layout.addWidget(self.filename_label)
        layout.addWidget(self.image_type_label)
        layout.addWidget(self.image_type_combobox)
        layout.addWidget(self.ok_button)
        self.setLayout(layout)

        self.ok_button.clicked.connect(self.accept)

    def get_data(self):
        return [self.image_type_combobox.currentText(), self.filepath, ""] #last item is placeholder for comments


class DragAndDropBox(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Dialog Eigenschaften festlegen
        self.setWindowTitle("Drop your files here")
        self.setModal(True)

        self.returndata = []
        self.images = []
        # Widgets erstellen
        self.label1 = QLabel("Sample Name")

        self.sample_name_edit = QComboBox()
        self.sample_name_edit.setEditable(True)
        self.label = QLabel("Drop your files here")
        self.list_widget = QListWidget()
        self.ok_button = QPushButton("Okay")

        # Layout erstellen
        layout = QVBoxLayout()
        layout.addWidget(self.label1)
        layout.addWidget(self.sample_name_edit)
        layout.addWidget(self.label)
        layout.addWidget(self.list_widget)
        layout.addWidget(self.ok_button)

        # Layout dem Dialog zuweisen
        self.setLayout(layout)

        # "Drop-Zone" kennzeichnen
        self.setAcceptDrops(True)

        # Signal-Slot-Verbindungen herstellen
        self.ok_button.clicked.connect(self.accept)
        liste = [self.sample_name_edit,self.label1,self.label, self.list_widget,self.ok_button]
        for element in liste: element.setFont(QFont('Arial', 16))
        self.list_widget.setIconSize(QSize(48, 48)) # Größe der Icons auf 48x48 Pixel setzen

    def dragEnterEvent(self, event: QDragEnterEvent):
        # Überprüfen, ob es sich um eine Datei handelt
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event: QDropEvent):
        # Liste der Dateien hinzufügen
        for url in event.mimeData().urls():
            file_path = url.toLocalFile()

            self.returndata.append(file_path)
            file_name = file_path.split("/")[-1]
            # print(file_path)
            item = QListWidgetItem(file_name)

            # Unterschiedliche Aktionen für unterschiedliche Dateitypen
            if file_name.endswith('.png') or file_name.endswith('.tif') or file_name.endswith('.tiff') or file_name.endswith('.jpg'):
                image_dialog = ImageTypeDialog(file_path, parent=self)
                if image_dialog.exec():
                    returndata = image_dialog.get_data()
                    self.list_widget.addItem(item)
                    self.images.append(returndata)

            elif file_name.endswith('.csw'):
                self.list_widget.addItem(item)
                pixmap = QPixmap("cs.png")
                icon = pixmap.scaled(50, 50, Qt.KeepAspectRatio, Qt.SmoothTransformation)
                item.setIcon(icon)
                item.setText('[Cryoscan] ' + file_name)
                self.returndata.append(["cryoscan", file_path, ""])

            elif file_name.endswith('.txt'):
                # typeof = checktxt(file_path)
                self.list_widget.addItem(item)
                item.setText('[txt]: ' + file_name)
                self.returndata.append(["txt", file_path, ""])
                
        self.returndata.append(["images",self.images])
        return self.returndata

    def get_data(self):
        # Liste der Dateien und Sample-Name zurückgeben
        # files = [self.list_widget.item(i).text() for i in range(self.list_widget.count())]
        sample_name = self.sample_name_edit.currentText()
        return sample_name, self.returndata


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Fenster Eigenschaften festlegen
        self.setWindowTitle("Hauptfenster")
        self.setGeometry(100, 100, 500, 500)

        # Widgets erstellen
        self.load_data_button = QPushButton("Daten laden")

        # Layout erstellen
        layout = QHBoxLayout()
        layout.addWidget(self.load_data_button)

        # Layout dem Fenster zuweisen
        self.setLayout(layout)

        # Signal-Slot-Verbindungen herstellen
        self.load_data_button.clicked.connect(self.show_drag_and_drop_box)

    def show_drag_and_drop_box(self):
        # Dialog für Drag-and-Drop-Box erstellen und anzeigen
        dialog = DragAndDropBox(parent=self)
        if dialog.exec():
            sample_name, files = dialog.get_data()
            print("Sample-Name:", sample_name)
            print("Dateien:", files)
            for file in files:
                print(file)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    font = QFont()
    font.setPointSize(16)
    app.setFont(font)

    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())