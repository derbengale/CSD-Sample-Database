import sys
from PySide6.QtCore import Qt, QRect 
from PySide6.QtGui import QPixmap, QPainter, QPen, QFont
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout,QHBoxLayout, QWidget, QFileDialog, QScrollArea,QSlider

class ImageWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.marked_rects = []
        self._pixmap = QPixmap()
        self._scale_factor = 1.0  # initialize the scale factor to 1.0

    def setPixmap(self, pixmap):
        self._pixmap = pixmap
        super().setFixedSize(pixmap.size() * self._scale_factor)  # scale the widget size
        self.update()

    def pixmap(self):
        return self._pixmap

    def set_scale_factor(self, scale_factor):
        self._scale_factor = scale_factor
        self.setFixedSize(self.pixmap().size() * self._scale_factor)  # scale the widget size
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(self.rect(), self.pixmap())

        pen = QPen(Qt.red, 2 / self._scale_factor, Qt.SolidLine)  # scale the pen width
        painter.setPen(pen)

        for rect in self.marked_rects:
            scaled_rect = QRect(rect.topLeft() * self._scale_factor, rect.bottomRight() * self._scale_factor)
            painter.drawRect(scaled_rect)

    def mousePressEvent(self, event):
        self.start_pos = event.position()

    def mouseReleaseEvent(self, event):
        end_pos = event.position()
        rect = self.get_rect(self.start_pos, end_pos)
        if rect.width() > 0 and rect.height() > 0:
            self.marked_rects.append(rect)
            self.update()

    def get_rect(self, start_pos, end_pos):
        scaled_start_pos = start_pos * (1 / self._scale_factor)
        scaled_end_pos = end_pos * (1 / self._scale_factor)
        x1 = min(scaled_start_pos.x(), scaled_end_pos.x())
        y1 = min(scaled_start_pos.y(), scaled_end_pos.y())
        x2 = max(scaled_start_pos.x(), scaled_end_pos.x())
        y2 = max(scaled_start_pos.y(), scaled_end_pos.y())

        return QRect(x1, y1, x2 - x1, y2 - y1)
    
class crop_module(QMainWindow):
    def __init__(self):
        super().__init__()
        
        print("Opening crop module...")
        # Create widgets
        self.image_widget = ImageWidget()
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidget(self.image_widget)
        self.scroll_area.setWidgetResizable(True)
        self.load_button = QPushButton("Load Image")
        self.save_button = QPushButton("Save Marked Rects")
        self.remove_button = QPushButton("Remove Last Rect")
        self.remove_all_button = QPushButton("Remove All Rects")
        self.zoom_slider = QSlider(Qt.Horizontal)  # create a horizontal slider for zooming
        self.zoom_slider.setMinimum(1)
        self.zoom_slider.setMaximum(10)
        self.zoom_slider.setValue(5)

        font = QFont("Courier New", 20)

        # Create layout
        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.load_button)
        hbox1.addWidget(self.save_button)

        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.remove_button)
        hbox2.addWidget(self.remove_all_button)

        vbox = QVBoxLayout()
        vbox.addWidget(self.scroll_area)
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addWidget(self.zoom_slider)  # add the zoom slider to the layout

        widget = QWidget()
        widget.setLayout(vbox)

        self.setCentralWidget(widget)
        self.setWindowTitle("Image Cropping Module")
        self.showMaximized()

        # Connect signals
        self.load_button.clicked.connect(self.load_image)
        self.save_button.clicked.connect(self.save_rects)
        self.remove_button.clicked.connect(self.remove_last_rect)
        self.remove_all_button.clicked.connect(self.remove_all_rects)
        self.zoom_slider.valueChanged.connect(self.update_zoom)  # connect the slider signal

    def load_image(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Open Image File", ".", "Image Files (*.png *.jpg *.bmp)"
        )
        if file_path:
            pixmap = QPixmap(file_path)
            self.image_widget.setPixmap(pixmap)

        import os
        self.file_name = os.path.splitext(os.path.basename(file_path))[0]
        


    def save_rects(self):
        for i, rect in enumerate(self.image_widget.marked_rects):
            cropped_pixmap = self.image_widget.pixmap().copy(rect)
            cropped_pixmap.save(f"{self.file_name}_{i}.png")

    def remove_last_rect(self):
        if self.image_widget.marked_rects:
            self.image_widget.marked_rects.pop()
            self.image_widget.update()

    def remove_all_rects(self):
        self.image_widget.marked_rects.clear()
        self.image_widget.update()

    def update_zoom(self, value):
        scale_factor = value / 5  # map the slider value to a scale factor between 0.2 and 2.0
        self.image_widget.set_scale_factor(scale_factor)
        self.scroll_area.setMinimumSize(self.image_widget.size())  # update the scroll area size to match the widget size


if __name__ == "__main__":
    font = QFont("Arial", 32)
    app = QApplication(sys.argv)
    app.setFont(font)

    window = crop_module()
    window.show()
    sys.exit(app.exec())