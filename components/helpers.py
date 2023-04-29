from PySide6.QtWidgets import QStyledItemDelegate, QComboBox
from PySide6.QtCore import Qt

def openfile(filepath):
    import subprocess, os, platform
    if platform.system() == 'Darwin':       # macOS
        subprocess.call(('open', filepath))
    elif platform.system() == 'Windows':    # Windows
        os.startfile(filepath)
    else:                                   # linux variants
        subprocess.call(('xdg-open', filepath))

class CenterDelegate(QStyledItemDelegate):
    
    def initStyleOption(self, option, index):
        super().initStyleOption(option, index)
        option.displayAlignment = Qt.AlignHCenter


def normalize_array(arr):
    arr_min = min(arr)
    arr_max = max(arr)
    return [(x - arr_min) / (arr_max - arr_min) for x in arr]


class StdoutRedirector:
    def __init__(self, text_edit):
        self.text_edit = text_edit
        self.buffer = ''

    def write(self, text):
        self.buffer += text
        if '\n' in self.buffer:
            lines = self.buffer.split('\n')
            for line in lines[:-1]:
                self.text_edit.append(line)
            self.buffer = lines[-1]

    def flush(self):
        if self.buffer:
            self.text_edit.append(self.buffer)
            self.buffer = ''


def remove_duplicates(lst):
    return list(set(lst))


def populate_combobox(items: list, combobox: QComboBox, add_all=True):
    """
    Populate a QComboBox with the items in a list, if they do not already exist in the QComboBox.
    """
    if add_all == True: combobox.addItem("All")
    for item in items:
        if not combobox.findText(item) >= 0:
            combobox.addItem(item)