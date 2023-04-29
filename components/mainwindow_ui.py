# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLayout, QLineEdit, QListView, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QSpinBox, QStatusBar, QTabWidget, QTableView,
    QTableWidget, QTableWidgetItem, QTextEdit, QToolBar,
    QVBoxLayout, QWidget)

from components.mplwidget import MplWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(2196, 1689)
        self.actionDatenbank_sichern = QAction(MainWindow)
        self.actionDatenbank_sichern.setObjectName(u"actionDatenbank_sichern")
        self.actionImage_Crop_Module = QAction(MainWindow)
        self.actionImage_Crop_Module.setObjectName(u"actionImage_Crop_Module")
        self.show_comparator = QAction(MainWindow)
        self.show_comparator.setObjectName(u"show_comparator")
        self.actionHaar_Casacade_Trainer = QAction(MainWindow)
        self.actionHaar_Casacade_Trainer.setObjectName(u"actionHaar_Casacade_Trainer")
        self.actionDatenbank_Editor = QAction(MainWindow)
        self.actionDatenbank_Editor.setObjectName(u"actionDatenbank_Editor")
        self.actionDatenbank_Ciewer = QAction(MainWindow)
        self.actionDatenbank_Ciewer.setObjectName(u"actionDatenbank_Ciewer")
        self.actionLog = QAction(MainWindow)
        self.actionLog.setObjectName(u"actionLog")
        self.actionGithub_Link = QAction(MainWindow)
        self.actionGithub_Link.setObjectName(u"actionGithub_Link")
        self.actionBenutzer_hinzuf_gen = QAction(MainWindow)
        self.actionBenutzer_hinzuf_gen.setObjectName(u"actionBenutzer_hinzuf_gen")
        self.actionBenutzer_Archivieren = QAction(MainWindow)
        self.actionBenutzer_Archivieren.setObjectName(u"actionBenutzer_Archivieren")
        self.actionDatenbankstruktur_Exportieren = QAction(MainWindow)
        self.actionDatenbankstruktur_Exportieren.setObjectName(u"actionDatenbankstruktur_Exportieren")
        self.actionSettings_ini = QAction(MainWindow)
        self.actionSettings_ini.setObjectName(u"actionSettings_ini")
        self.actionHelp_to_Translate = QAction(MainWindow)
        self.actionHelp_to_Translate.setObjectName(u"actionHelp_to_Translate")
        self.actionEdit_Haar_Classifiers = QAction(MainWindow)
        self.actionEdit_Haar_Classifiers.setObjectName(u"actionEdit_Haar_Classifiers")
        self.centralWidget = QWidget(MainWindow)
        self.centralWidget.setObjectName(u"centralWidget")
        self.gridLayout_2 = QGridLayout(self.centralWidget)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setSizeConstraint(QLayout.SetMinimumSize)
        self.result_list = QListView(self.centralWidget)
        self.result_list.setObjectName(u"result_list")
        self.result_list.setMaximumSize(QSize(200, 16777215))

        self.verticalLayout_6.addWidget(self.result_list)

        self.add_files = QPushButton(self.centralWidget)
        self.add_files.setObjectName(u"add_files")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_files.sizePolicy().hasHeightForWidth())
        self.add_files.setSizePolicy(sizePolicy)
        self.add_files.setMinimumSize(QSize(0, 50))
        self.add_files.setMaximumSize(QSize(200, 16777215))
        font = QFont()
        font.setPointSize(18)
        self.add_files.setFont(font)

        self.verticalLayout_6.addWidget(self.add_files)


        self.horizontalLayout_6.addLayout(self.verticalLayout_6)

        self.tabWidget = QTabWidget(self.centralWidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setEnabled(True)
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Emoji"])
        self.tabWidget.setFont(font1)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.images = QWidget()
        self.images.setObjectName(u"images")
        self.gridLayout_6 = QGridLayout(self.images)
        self.gridLayout_6.setSpacing(6)
        self.gridLayout_6.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setSpacing(6)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.selector_image = QComboBox(self.images)
        self.selector_image.addItem("")
        self.selector_image.addItem("")
        self.selector_image.addItem("")
        self.selector_image.addItem("")
        self.selector_image.addItem("")
        self.selector_image.addItem("")
        self.selector_image.addItem("")
        self.selector_image.addItem("")
        self.selector_image.setObjectName(u"selector_image")

        self.verticalLayout_7.addWidget(self.selector_image)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setSpacing(6)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.picture_screen = QLabel(self.images)
        self.picture_screen.setObjectName(u"picture_screen")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.picture_screen.sizePolicy().hasHeightForWidth())
        self.picture_screen.setSizePolicy(sizePolicy1)
        self.picture_screen.setMinimumSize(QSize(500, 500))
        self.picture_screen.setScaledContents(False)
        self.picture_screen.setAlignment(Qt.AlignCenter)
        self.picture_screen.setWordWrap(True)

        self.horizontalLayout_10.addWidget(self.picture_screen)


        self.verticalLayout_7.addLayout(self.horizontalLayout_10)

        self.frame = QFrame(self.images)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 52))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.frame)
        self.gridLayout_9.setSpacing(6)
        self.gridLayout_9.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(6)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.pushButton_7 = QPushButton(self.frame)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_7.addWidget(self.pushButton_7)

        self.analyze_color = QPushButton(self.frame)
        self.analyze_color.setObjectName(u"analyze_color")
        self.analyze_color.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_7.addWidget(self.analyze_color)


        self.gridLayout_9.addLayout(self.horizontalLayout_7, 1, 0, 1, 1)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setSpacing(6)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.image_previous = QPushButton(self.frame)
        self.image_previous.setObjectName(u"image_previous")
        self.image_previous.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_15.addWidget(self.image_previous)

        self.image_next = QPushButton(self.frame)
        self.image_next.setObjectName(u"image_next")
        self.image_next.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_15.addWidget(self.image_next)


        self.gridLayout_9.addLayout(self.horizontalLayout_15, 0, 0, 1, 1)


        self.verticalLayout_7.addWidget(self.frame)


        self.gridLayout_6.addLayout(self.verticalLayout_7, 0, 0, 1, 1)

        self.tabWidget.addTab(self.images, "")
        self.CSD = QWidget()
        self.CSD.setObjectName(u"CSD")
        self.gridLayout_8 = QGridLayout(self.CSD)
        self.gridLayout_8.setSpacing(6)
        self.gridLayout_8.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.plot_csd = MplWidget(self.CSD)
        self.plot_csd.setObjectName(u"plot_csd")
        self.plot_csd.setMinimumSize(QSize(600, 600))

        self.gridLayout_8.addWidget(self.plot_csd, 1, 0, 1, 1)

        self.selector_image_4 = QComboBox(self.CSD)
        self.selector_image_4.addItem("")
        self.selector_image_4.addItem("")
        self.selector_image_4.addItem("")
        self.selector_image_4.addItem("")
        self.selector_image_4.setObjectName(u"selector_image_4")

        self.gridLayout_8.addWidget(self.selector_image_4, 0, 0, 1, 1)

        self.tabWidget.addTab(self.CSD, "")
        self.jcsf = QWidget()
        self.jcsf.setObjectName(u"jcsf")
        self.verticalLayout = QVBoxLayout(self.jcsf)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.plot_jcsf = MplWidget(self.jcsf)
        self.plot_jcsf.setObjectName(u"plot_jcsf")
        sizePolicy1.setHeightForWidth(self.plot_jcsf.sizePolicy().hasHeightForWidth())
        self.plot_jcsf.setSizePolicy(sizePolicy1)
        self.plot_jcsf.setMinimumSize(QSize(600, 600))

        self.verticalLayout.addWidget(self.plot_jcsf)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label = QLabel(self.jcsf)
        self.label.setObjectName(u"label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy2)
        self.label.setMaximumSize(QSize(16777215, 30))
        self.label.setFrameShape(QFrame.Panel)
        self.label.setFrameShadow(QFrame.Plain)
        self.label.setTextFormat(Qt.RichText)
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label)

        self.v_sc = QLabel(self.jcsf)
        self.v_sc.setObjectName(u"v_sc")
        sizePolicy2.setHeightForWidth(self.v_sc.sizePolicy().hasHeightForWidth())
        self.v_sc.setSizePolicy(sizePolicy2)
        self.v_sc.setMaximumSize(QSize(16777215, 30))
        self.v_sc.setFrameShape(QFrame.Panel)
        self.v_sc.setFrameShadow(QFrame.Raised)
        self.v_sc.setTextFormat(Qt.RichText)
        self.v_sc.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.v_sc)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_2 = QLabel(self.jcsf)
        self.label_2.setObjectName(u"label_2")
        sizePolicy2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy2)
        self.label_2.setMaximumSize(QSize(16777215, 30))
        self.label_2.setFrameShape(QFrame.Panel)
        self.label_2.setFrameShadow(QFrame.Plain)
        self.label_2.setTextFormat(Qt.RichText)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_2)

        self.v_cumul_score = QLabel(self.jcsf)
        self.v_cumul_score.setObjectName(u"v_cumul_score")
        sizePolicy2.setHeightForWidth(self.v_cumul_score.sizePolicy().hasHeightForWidth())
        self.v_cumul_score.setSizePolicy(sizePolicy2)
        self.v_cumul_score.setMaximumSize(QSize(16777215, 30))
        self.v_cumul_score.setFrameShape(QFrame.Panel)
        self.v_cumul_score.setFrameShadow(QFrame.Raised)
        self.v_cumul_score.setTextFormat(Qt.RichText)
        self.v_cumul_score.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.v_cumul_score)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.jcsf)
        self.label_3.setObjectName(u"label_3")
        sizePolicy2.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy2)
        self.label_3.setMaximumSize(QSize(16777215, 30))
        self.label_3.setFrameShape(QFrame.Panel)
        self.label_3.setFrameShadow(QFrame.Plain)
        self.label_3.setTextFormat(Qt.RichText)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_3)

        self.v_std = QLabel(self.jcsf)
        self.v_std.setObjectName(u"v_std")
        sizePolicy2.setHeightForWidth(self.v_std.sizePolicy().hasHeightForWidth())
        self.v_std.setSizePolicy(sizePolicy2)
        self.v_std.setMaximumSize(QSize(16777215, 30))
        self.v_std.setFrameShape(QFrame.Panel)
        self.v_std.setFrameShadow(QFrame.Raised)
        self.v_std.setTextFormat(Qt.RichText)
        self.v_std.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.v_std)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_7 = QLabel(self.jcsf)
        self.label_7.setObjectName(u"label_7")
        sizePolicy2.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy2)
        self.label_7.setMaximumSize(QSize(16777215, 30))
        self.label_7.setFrameShape(QFrame.Panel)
        self.label_7.setFrameShadow(QFrame.Plain)
        self.label_7.setTextFormat(Qt.RichText)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_7)

        self.v_std_2 = QLabel(self.jcsf)
        self.v_std_2.setObjectName(u"v_std_2")
        sizePolicy2.setHeightForWidth(self.v_std_2.sizePolicy().hasHeightForWidth())
        self.v_std_2.setSizePolicy(sizePolicy2)
        self.v_std_2.setMaximumSize(QSize(16777215, 30))
        self.v_std_2.setFrameShape(QFrame.Panel)
        self.v_std_2.setFrameShadow(QFrame.Raised)
        self.v_std_2.setTextFormat(Qt.RichText)
        self.v_std_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.v_std_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_8 = QLabel(self.jcsf)
        self.label_8.setObjectName(u"label_8")
        sizePolicy2.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy2)
        self.label_8.setMaximumSize(QSize(16777215, 30))
        self.label_8.setFrameShape(QFrame.Panel)
        self.label_8.setFrameShadow(QFrame.Plain)
        self.label_8.setTextFormat(Qt.RichText)
        self.label_8.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_8)

        self.v_std_3 = QLabel(self.jcsf)
        self.v_std_3.setObjectName(u"v_std_3")
        sizePolicy2.setHeightForWidth(self.v_std_3.sizePolicy().hasHeightForWidth())
        self.v_std_3.setSizePolicy(sizePolicy2)
        self.v_std_3.setMaximumSize(QSize(16777215, 30))
        self.v_std_3.setFrameShape(QFrame.Panel)
        self.v_std_3.setFrameShadow(QFrame.Raised)
        self.v_std_3.setTextFormat(Qt.RichText)
        self.v_std_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.v_std_3)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.comboBox = QComboBox(self.jcsf)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.verticalLayout.addWidget(self.comboBox)

        self.tabWidget.addTab(self.jcsf, "")
        self.tcind = QWidget()
        self.tcind.setObjectName(u"tcind")
        self.gridLayout_4 = QGridLayout(self.tcind)
        self.gridLayout_4.setSpacing(6)
        self.gridLayout_4.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.plot_tc_ppms = MplWidget(self.tcind)
        self.plot_tc_ppms.setObjectName(u"plot_tc_ppms")
        self.plot_tc_ppms.setMinimumSize(QSize(600, 600))

        self.gridLayout_4.addWidget(self.plot_tc_ppms, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tcind, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_5 = QGridLayout(self.tab)
        self.gridLayout_5.setSpacing(6)
        self.gridLayout_5.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.plot_xrd = MplWidget(self.tab)
        self.plot_xrd.setObjectName(u"plot_xrd")
        self.plot_xrd.setMinimumSize(QSize(600, 600))

        self.gridLayout_5.addWidget(self.plot_xrd, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.filter = QWidget()
        self.filter.setObjectName(u"filter")
        self.gridLayout_14 = QGridLayout(self.filter)
        self.gridLayout_14.setSpacing(6)
        self.gridLayout_14.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setSpacing(6)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_13 = QLabel(self.filter)
        self.label_13.setObjectName(u"label_13")
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(28)
        self.label_13.setFont(font2)
        self.label_13.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.label_13)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setSpacing(6)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setSpacing(6)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setSpacing(6)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_10 = QLabel(self.filter)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_12.addWidget(self.label_10)

        self.search_user = QComboBox(self.filter)
        self.search_user.setObjectName(u"search_user")

        self.horizontalLayout_12.addWidget(self.search_user)


        self.verticalLayout_14.addLayout(self.horizontalLayout_12)

        self.listView = QListView(self.filter)
        self.listView.setObjectName(u"listView")

        self.verticalLayout_14.addWidget(self.listView)


        self.horizontalLayout_14.addLayout(self.verticalLayout_14)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setSpacing(6)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setSpacing(6)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_11 = QLabel(self.filter)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_13.addWidget(self.label_11)

        self.search_element = QComboBox(self.filter)
        self.search_element.setObjectName(u"search_element")

        self.horizontalLayout_13.addWidget(self.search_element)


        self.verticalLayout_13.addLayout(self.horizontalLayout_13)

        self.listView_2 = QListView(self.filter)
        self.listView_2.setObjectName(u"listView_2")

        self.verticalLayout_13.addWidget(self.listView_2)


        self.horizontalLayout_14.addLayout(self.verticalLayout_13)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setSpacing(6)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setSpacing(6)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_12 = QLabel(self.filter)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_11.addWidget(self.label_12)

        self.frame_3 = QFrame(self.filter)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.frame_3.setLineWidth(6)
        self.gridLayout_13 = QGridLayout(self.frame_3)
        self.gridLayout_13.setSpacing(6)
        self.gridLayout_13.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setSpacing(6)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.checkBox = QCheckBox(self.frame_3)
        self.checkBox.setObjectName(u"checkBox")

        self.horizontalLayout_11.addWidget(self.checkBox)

        self.checkBox_2 = QCheckBox(self.frame_3)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.horizontalLayout_11.addWidget(self.checkBox_2)

        self.checkBox_3 = QCheckBox(self.frame_3)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.horizontalLayout_11.addWidget(self.checkBox_3)

        self.checkBox_4 = QCheckBox(self.frame_3)
        self.checkBox_4.setObjectName(u"checkBox_4")

        self.horizontalLayout_11.addWidget(self.checkBox_4)


        self.gridLayout_13.addLayout(self.horizontalLayout_11, 0, 0, 1, 1)


        self.verticalLayout_11.addWidget(self.frame_3)


        self.verticalLayout_12.addLayout(self.verticalLayout_11)

        self.listView_3 = QListView(self.filter)
        self.listView_3.setObjectName(u"listView_3")

        self.verticalLayout_12.addWidget(self.listView_3)


        self.horizontalLayout_14.addLayout(self.verticalLayout_12)


        self.verticalLayout_15.addLayout(self.horizontalLayout_14)

        self.label_14 = QLabel(self.filter)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font2)
        self.label_14.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.label_14)

        self.listView_4 = QListView(self.filter)
        self.listView_4.setObjectName(u"listView_4")

        self.verticalLayout_15.addWidget(self.listView_4)

        self.label_15 = QLabel(self.filter)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font2)
        self.label_15.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.label_15)

        self.listView_5 = QListView(self.filter)
        self.listView_5.setObjectName(u"listView_5")

        self.verticalLayout_15.addWidget(self.listView_5)


        self.gridLayout_14.addLayout(self.verticalLayout_15, 0, 0, 1, 1)

        self.tabWidget.addTab(self.filter, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout = QGridLayout(self.tab_2)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(6)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_4 = QLabel(self.tab_2)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_8.addWidget(self.label_4)

        self.key_edit = QLineEdit(self.tab_2)
        self.key_edit.setObjectName(u"key_edit")

        self.horizontalLayout_8.addWidget(self.key_edit)

        self.label_5 = QLabel(self.tab_2)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_8.addWidget(self.label_5)

        self.min_edit = QLineEdit(self.tab_2)
        self.min_edit.setObjectName(u"min_edit")

        self.horizontalLayout_8.addWidget(self.min_edit)

        self.label_6 = QLabel(self.tab_2)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_8.addWidget(self.label_6)

        self.max_edit = QLineEdit(self.tab_2)
        self.max_edit.setObjectName(u"max_edit")

        self.horizontalLayout_8.addWidget(self.max_edit)

        self.dsd_okay_button = QPushButton(self.tab_2)
        self.dsd_okay_button.setObjectName(u"dsd_okay_button")

        self.horizontalLayout_8.addWidget(self.dsd_okay_button)

        self.label_16 = QLabel(self.tab_2)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_8.addWidget(self.label_16)

        self.nFakeFactors = QSpinBox(self.tab_2)
        self.nFakeFactors.setObjectName(u"nFakeFactors")

        self.horizontalLayout_8.addWidget(self.nFakeFactors)


        self.verticalLayout_2.addLayout(self.horizontalLayout_8)

        self.dsdTable = QTableWidget(self.tab_2)
        if (self.dsdTable.columnCount() < 3):
            self.dsdTable.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.dsdTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.dsdTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.dsdTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.dsdTable.setObjectName(u"dsdTable")

        self.verticalLayout_2.addWidget(self.dsdTable)

        self.dsd_result = QTextEdit(self.tab_2)
        self.dsd_result.setObjectName(u"dsd_result")
        self.dsd_result.setEnabled(False)
        self.dsd_result.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.dsd_result.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.dsd_result.setUndoRedoEnabled(False)
        self.dsd_result.setReadOnly(True)

        self.verticalLayout_2.addWidget(self.dsd_result)


        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")
        self.db = QWidget()
        self.db.setObjectName(u"db")
        self.gridLayout_3 = QGridLayout(self.db)
        self.gridLayout_3.setSpacing(6)
        self.gridLayout_3.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(6)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setSpacing(6)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_9 = QLabel(self.db)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(200, 16777215))
        self.label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_9)

        self.table_selector = QListView(self.db)
        self.table_selector.setObjectName(u"table_selector")
        self.table_selector.setMaximumSize(QSize(200, 16777215))

        self.verticalLayout_10.addWidget(self.table_selector)


        self.horizontalLayout_9.addLayout(self.verticalLayout_10)

        self.db_table = QTableView(self.db)
        self.db_table.setObjectName(u"db_table")

        self.horizontalLayout_9.addWidget(self.db_table)


        self.gridLayout_3.addLayout(self.horizontalLayout_9, 0, 0, 1, 1)

        self.tabWidget.addTab(self.db, "")
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.gridLayout_11 = QGridLayout(self.tab_7)
        self.gridLayout_11.setSpacing(6)
        self.gridLayout_11.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.log = QTextEdit(self.tab_7)
        self.log.setObjectName(u"log")
        self.log.setEnabled(True)
        self.log.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.log.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.log.setUndoRedoEnabled(False)
        self.log.setReadOnly(True)

        self.gridLayout_11.addWidget(self.log, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_7, "")

        self.horizontalLayout_6.addWidget(self.tabWidget)


        self.gridLayout_2.addLayout(self.horizontalLayout_6, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 2196, 22))
        self.menuDatei = QMenu(self.menuBar)
        self.menuDatei.setObjectName(u"menuDatei")
        self.menuDatenbank = QMenu(self.menuBar)
        self.menuDatenbank.setObjectName(u"menuDatenbank")
        self.menuExtras = QMenu(self.menuBar)
        self.menuExtras.setObjectName(u"menuExtras")
        self.menuHelp = QMenu(self.menuBar)
        self.menuHelp.setObjectName(u"menuHelp")
        self.menuBenutzer = QMenu(self.menuBar)
        self.menuBenutzer.setObjectName(u"menuBenutzer")
        self.menuBackup = QMenu(self.menuBar)
        self.menuBackup.setObjectName(u"menuBackup")
        self.menuSprache = QMenu(self.menuBar)
        self.menuSprache.setObjectName(u"menuSprache")
        self.menuEinstellungen = QMenu(self.menuBar)
        self.menuEinstellungen.setObjectName(u"menuEinstellungen")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QToolBar(MainWindow)
        self.mainToolBar.setObjectName(u"mainToolBar")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.menuBar.addAction(self.menuDatei.menuAction())
        self.menuBar.addAction(self.menuDatenbank.menuAction())
        self.menuBar.addAction(self.menuExtras.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())
        self.menuBar.addAction(self.menuBenutzer.menuAction())
        self.menuBar.addAction(self.menuBackup.menuAction())
        self.menuBar.addAction(self.menuSprache.menuAction())
        self.menuBar.addAction(self.menuEinstellungen.menuAction())
        self.menuDatenbank.addAction(self.actionDatenbank_sichern)
        self.menuDatenbank.addAction(self.actionDatenbank_Editor)
        self.menuDatenbank.addAction(self.actionDatenbank_Ciewer)
        self.menuExtras.addAction(self.actionImage_Crop_Module)
        self.menuExtras.addAction(self.show_comparator)
        self.menuExtras.addAction(self.actionHaar_Casacade_Trainer)
        self.menuExtras.addAction(self.actionLog)
        self.menuHelp.addAction(self.actionGithub_Link)
        self.menuHelp.addAction(self.actionHelp_to_Translate)
        self.menuBenutzer.addAction(self.actionBenutzer_hinzuf_gen)
        self.menuBenutzer.addAction(self.actionBenutzer_Archivieren)
        self.menuBackup.addAction(self.actionDatenbankstruktur_Exportieren)
        self.menuEinstellungen.addAction(self.actionSettings_ini)
        self.menuEinstellungen.addAction(self.actionEdit_Haar_Classifiers)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(7)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionDatenbank_sichern.setText(QCoreApplication.translate("MainWindow", u"Datenbank sichern", None))
        self.actionImage_Crop_Module.setText(QCoreApplication.translate("MainWindow", u"Image Crop Module", None))
        self.show_comparator.setText(QCoreApplication.translate("MainWindow", u"Microscope Image Comparator", None))
        self.actionHaar_Casacade_Trainer.setText(QCoreApplication.translate("MainWindow", u"Haar Casacade Trainer", None))
        self.actionDatenbank_Editor.setText(QCoreApplication.translate("MainWindow", u"Datenbank Editor", None))
        self.actionDatenbank_Ciewer.setText(QCoreApplication.translate("MainWindow", u"Datenbank Viewer", None))
        self.actionLog.setText(QCoreApplication.translate("MainWindow", u"Log", None))
        self.actionGithub_Link.setText(QCoreApplication.translate("MainWindow", u"Github Link", None))
        self.actionBenutzer_hinzuf_gen.setText(QCoreApplication.translate("MainWindow", u"Benutzer hinzuf\u00fcgen", None))
        self.actionBenutzer_Archivieren.setText(QCoreApplication.translate("MainWindow", u"Benutzer Archivieren", None))
        self.actionDatenbankstruktur_Exportieren.setText(QCoreApplication.translate("MainWindow", u"Datenbankstruktur Exportieren", None))
        self.actionSettings_ini.setText(QCoreApplication.translate("MainWindow", u"Settings.ini", None))
        self.actionHelp_to_Translate.setText(QCoreApplication.translate("MainWindow", u"Help to Translate", None))
        self.actionEdit_Haar_Classifiers.setText(QCoreApplication.translate("MainWindow", u"Edit Haar Classifiers", None))
        self.add_files.setText(QCoreApplication.translate("MainWindow", u"Add Files", None))
        self.selector_image.setItemText(0, QCoreApplication.translate("MainWindow", u"Light Microscope (overview)", None))
        self.selector_image.setItemText(1, QCoreApplication.translate("MainWindow", u"Light Microscope (details)", None))
        self.selector_image.setItemText(2, QCoreApplication.translate("MainWindow", u"REM (500x)", None))
        self.selector_image.setItemText(3, QCoreApplication.translate("MainWindow", u"REM (1000x)", None))
        self.selector_image.setItemText(4, QCoreApplication.translate("MainWindow", u"REM (2000x)", None))
        self.selector_image.setItemText(5, QCoreApplication.translate("MainWindow", u"REM (5000x)", None))
        self.selector_image.setItemText(6, QCoreApplication.translate("MainWindow", u"REM (details)", None))
        self.selector_image.setItemText(7, QCoreApplication.translate("MainWindow", u"REM (EBSD)", None))

        self.picture_screen.setText(QCoreApplication.translate("MainWindow", u"Picture here", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Haar Cascades", None))
        self.analyze_color.setText(QCoreApplication.translate("MainWindow", u"Calculate Hue Factor", None))
        self.image_previous.setText(QCoreApplication.translate("MainWindow", u"Previous Image", None))
        self.image_next.setText(QCoreApplication.translate("MainWindow", u"Next Image", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.images), QCoreApplication.translate("MainWindow", u"Images", None))
        self.selector_image_4.setItemText(0, QCoreApplication.translate("MainWindow", u"Annealing", None))
        self.selector_image_4.setItemText(1, QCoreApplication.translate("MainWindow", u"Pyrolysis", None))
        self.selector_image_4.setItemText(2, QCoreApplication.translate("MainWindow", u"Crystallization", None))
        self.selector_image_4.setItemText(3, QCoreApplication.translate("MainWindow", u"Full Program", None))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.CSD), QCoreApplication.translate("MainWindow", u"CSD", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Superconducting Points", None))
        self.v_sc.setText(QCoreApplication.translate("MainWindow", u"Superconducting Points", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Cumulated y''_max", None))
        self.v_cumul_score.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Std(Jc) (SC Points)", None))
        self.v_std.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Linear Behaviour", None))
        self.v_std_2.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Not steep enough", None))
        self.v_std_3.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Raw Data", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Raw + Power Law Fit", None))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.jcsf), QCoreApplication.translate("MainWindow", u"Jc, self field", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tcind), QCoreApplication.translate("MainWindow", u"Tc PPMS", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Ranking", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"XRD", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Filter", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"User", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Element", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Must Contain", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Image", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"Jc", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"Tc", None))
        self.checkBox_4.setText(QCoreApplication.translate("MainWindow", u"XRD", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Sort by", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"2. sorting", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.filter), QCoreApplication.translate("MainWindow", u"Filter", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Variable", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Miniumum", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Maximum", None))
        self.dsd_okay_button.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Added Fake Factors", None))
        ___qtablewidgetitem = self.dsdTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Variable", None));
        ___qtablewidgetitem1 = self.dsdTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Neue Spalte", None));
        ___qtablewidgetitem2 = self.dsdTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Maximum", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"DSD", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Select Table", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.db), QCoreApplication.translate("MainWindow", u"Database", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), QCoreApplication.translate("MainWindow", u"Log", None))
        self.menuDatei.setTitle(QCoreApplication.translate("MainWindow", u"Datei", None))
        self.menuDatenbank.setTitle(QCoreApplication.translate("MainWindow", u"Datenbank", None))
        self.menuExtras.setTitle(QCoreApplication.translate("MainWindow", u"Extras", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
        self.menuBenutzer.setTitle(QCoreApplication.translate("MainWindow", u"Benutzer", None))
        self.menuBackup.setTitle(QCoreApplication.translate("MainWindow", u"Backup", None))
        self.menuSprache.setTitle(QCoreApplication.translate("MainWindow", u"Sprache", None))
        self.menuEinstellungen.setTitle(QCoreApplication.translate("MainWindow", u"Einstellungen", None))
    # retranslateUi

