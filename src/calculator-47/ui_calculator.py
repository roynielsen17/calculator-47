# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calculator.ui'
##
## Created by: Qt User Interface Compiler version 6.11.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QMainWindow,
    QMenuBar, QPushButton, QRadioButton, QSizePolicy,
    QSpacerItem, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1012, 950)
        font = QFont()
        font.setFamilies([u"Segoe UI Emoji"])
        MainWindow.setFont(font)
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(9, 0, 1001, 861))
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.frame = QFrame(self.frame_2)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(290, 0, 416, 411))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Emoji"])
        font1.setPointSize(18)
        self.frame.setFont(font1)
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.btn_7 = QPushButton(self.frame)
        self.btn_7.setObjectName(u"btn_7")
        self.btn_7.setFont(font1)

        self.gridLayout.addWidget(self.btn_7, 7, 0, 1, 3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 11, 0, 1, 1)

        self.btn_history = QPushButton(self.frame)
        self.btn_history.setObjectName(u"btn_history")
        font2 = QFont()
        font2.setFamilies([u"Segoe UI Emoji"])
        font2.setPointSize(16)
        self.btn_history.setFont(font2)
        icon = QIcon()
        icon.addFile(u"icons/history.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_history.setIcon(icon)
        self.btn_history.setIconSize(QSize(20, 20))

        self.gridLayout.addWidget(self.btn_history, 0, 8, 1, 1)

        self.btn_mplus = QPushButton(self.frame)
        self.btn_mplus.setObjectName(u"btn_mplus")
        font3 = QFont()
        font3.setFamilies([u"Segoe UI Emoji"])
        font3.setPointSize(13)
        self.btn_mplus.setFont(font3)

        self.gridLayout.addWidget(self.btn_mplus, 2, 4, 1, 1)

        self.btn_5 = QPushButton(self.frame)
        self.btn_5.setObjectName(u"btn_5")
        self.btn_5.setFont(font1)

        self.gridLayout.addWidget(self.btn_5, 8, 3, 1, 2)

        self.btn_dot = QPushButton(self.frame)
        self.btn_dot.setObjectName(u"btn_dot")
        self.btn_dot.setFont(font1)

        self.gridLayout.addWidget(self.btn_dot, 10, 5, 1, 2)

        self.btn_1 = QPushButton(self.frame)
        self.btn_1.setObjectName(u"btn_1")
        self.btn_1.setFont(font1)

        self.gridLayout.addWidget(self.btn_1, 9, 0, 1, 3)

        self.btn_mdown = QPushButton(self.frame)
        self.btn_mdown.setObjectName(u"btn_mdown")
        self.btn_mdown.setFont(font3)

        self.gridLayout.addWidget(self.btn_mdown, 2, 8, 1, 1)

        self.btn_clear = QPushButton(self.frame)
        self.btn_clear.setObjectName(u"btn_clear")
        font4 = QFont()
        font4.setFamilies([u"Cambria"])
        font4.setPointSize(18)
        self.btn_clear.setFont(font4)

        self.gridLayout.addWidget(self.btn_clear, 5, 5, 1, 2)

        self.btn_div = QPushButton(self.frame)
        self.btn_div.setObjectName(u"btn_div")
        self.btn_div.setFont(font4)

        self.gridLayout.addWidget(self.btn_div, 6, 7, 1, 2)

        self.btn_2 = QPushButton(self.frame)
        self.btn_2.setObjectName(u"btn_2")
        self.btn_2.setFont(font1)

        self.gridLayout.addWidget(self.btn_2, 9, 3, 1, 2)

        self.btn_sub = QPushButton(self.frame)
        self.btn_sub.setObjectName(u"btn_sub")
        font5 = QFont()
        font5.setFamilies([u"Segoe UI Emoji"])
        font5.setPointSize(7)
        self.btn_sub.setFont(font5)

        self.gridLayout.addWidget(self.btn_sub, 8, 7, 1, 2)

        self.btn_menu1 = QPushButton(self.frame)
        self.btn_menu1.setObjectName(u"btn_menu1")
        self.btn_menu1.setFont(font2)
        icon1 = QIcon()
        icon1.addFile(u"icons/dot.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_menu1.setIcon(icon1)
        self.btn_menu1.setIconSize(QSize(20, 20))

        self.gridLayout.addWidget(self.btn_menu1, 0, 0, 1, 1)

        self.btn_4 = QPushButton(self.frame)
        self.btn_4.setObjectName(u"btn_4")
        self.btn_4.setFont(font1)

        self.gridLayout.addWidget(self.btn_4, 8, 0, 1, 3)

        self.btn_add = QPushButton(self.frame)
        self.btn_add.setObjectName(u"btn_add")
        self.btn_add.setFont(font1)

        self.gridLayout.addWidget(self.btn_add, 9, 7, 1, 2)

        self.display = QLineEdit(self.frame)
        self.display.setObjectName(u"display")
        self.display.setFont(font1)

        self.gridLayout.addWidget(self.display, 1, 0, 1, 9)

        self.btn_reciprocal = QPushButton(self.frame)
        self.btn_reciprocal.setObjectName(u"btn_reciprocal")
        font6 = QFont()
        font6.setFamilies([u"Times New Roman"])
        font6.setPointSize(13)
        self.btn_reciprocal.setFont(font6)

        self.gridLayout.addWidget(self.btn_reciprocal, 6, 0, 1, 3)

        self.btn_mminus = QPushButton(self.frame)
        self.btn_mminus.setObjectName(u"btn_mminus")
        self.btn_mminus.setFont(font3)

        self.gridLayout.addWidget(self.btn_mminus, 2, 5, 1, 1)

        self.radioButton_octal = QRadioButton(self.frame)
        self.radioButton_octal.setObjectName(u"radioButton_octal")

        self.gridLayout.addWidget(self.radioButton_octal, 4, 1, 1, 2)

        self.btn_mul = QPushButton(self.frame)
        self.btn_mul.setObjectName(u"btn_mul")
        self.btn_mul.setFont(font1)

        self.gridLayout.addWidget(self.btn_mul, 7, 7, 1, 2)

        self.btn_equal = QPushButton(self.frame)
        self.btn_equal.setObjectName(u"btn_equal")
        self.btn_equal.setFont(font1)

        self.gridLayout.addWidget(self.btn_equal, 10, 7, 1, 2)

        self.btn_square = QPushButton(self.frame)
        self.btn_square.setObjectName(u"btn_square")
        font7 = QFont()
        font7.setFamilies([u"Cambria"])
        font7.setPointSize(13)
        self.btn_square.setFont(font7)

        self.gridLayout.addWidget(self.btn_square, 6, 3, 1, 2)

        self.btn_6 = QPushButton(self.frame)
        self.btn_6.setObjectName(u"btn_6")
        self.btn_6.setFont(font1)

        self.gridLayout.addWidget(self.btn_6, 8, 5, 1, 2)

        self.btn_percent = QPushButton(self.frame)
        self.btn_percent.setObjectName(u"btn_percent")
        self.btn_percent.setFont(font1)

        self.gridLayout.addWidget(self.btn_percent, 5, 0, 1, 3)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(10, 10))
        font8 = QFont()
        font8.setFamilies([u"Arial"])
        font8.setPointSize(18)
        self.label.setFont(font8)

        self.gridLayout.addWidget(self.label, 0, 1, 1, 4)

        self.btn_3 = QPushButton(self.frame)
        self.btn_3.setObjectName(u"btn_3")
        self.btn_3.setFont(font1)

        self.gridLayout.addWidget(self.btn_3, 9, 5, 1, 2)

        self.btn_sign = QPushButton(self.frame)
        self.btn_sign.setObjectName(u"btn_sign")
        font9 = QFont()
        font9.setFamilies([u"Segoe UI"])
        font9.setPointSize(18)
        self.btn_sign.setFont(font9)

        self.gridLayout.addWidget(self.btn_sign, 10, 0, 1, 3)

        self.btn_mc = QPushButton(self.frame)
        self.btn_mc.setObjectName(u"btn_mc")
        self.btn_mc.setFont(font3)

        self.gridLayout.addWidget(self.btn_mc, 2, 0, 1, 2)

        self.btn_ms = QPushButton(self.frame)
        self.btn_ms.setObjectName(u"btn_ms")
        self.btn_ms.setFont(font3)

        self.gridLayout.addWidget(self.btn_ms, 2, 6, 1, 2)

        self.btn_8 = QPushButton(self.frame)
        self.btn_8.setObjectName(u"btn_8")
        self.btn_8.setFont(font1)

        self.gridLayout.addWidget(self.btn_8, 7, 3, 1, 2)

        self.radioButton_decimal = QRadioButton(self.frame)
        self.radioButton_decimal.setObjectName(u"radioButton_decimal")

        self.gridLayout.addWidget(self.radioButton_decimal, 4, 0, 1, 1)

        self.btn_ce = QPushButton(self.frame)
        self.btn_ce.setObjectName(u"btn_ce")
        self.btn_ce.setFont(font4)

        self.gridLayout.addWidget(self.btn_ce, 5, 3, 1, 2)

        self.btn_sqrt = QPushButton(self.frame)
        self.btn_sqrt.setObjectName(u"btn_sqrt")
        self.btn_sqrt.setFont(font4)

        self.gridLayout.addWidget(self.btn_sqrt, 6, 5, 1, 2)

        self.btn_backspace = QPushButton(self.frame)
        self.btn_backspace.setObjectName(u"btn_backspace")
        self.btn_backspace.setFont(font1)

        self.gridLayout.addWidget(self.btn_backspace, 5, 7, 1, 2)

        self.btn_mr = QPushButton(self.frame)
        self.btn_mr.setObjectName(u"btn_mr")
        self.btn_mr.setFont(font3)

        self.gridLayout.addWidget(self.btn_mr, 2, 2, 1, 2)

        self.btn_0 = QPushButton(self.frame)
        self.btn_0.setObjectName(u"btn_0")
        self.btn_0.setFont(font1)

        self.gridLayout.addWidget(self.btn_0, 10, 3, 1, 2)

        self.btn_9 = QPushButton(self.frame)
        self.btn_9.setObjectName(u"btn_9")
        self.btn_9.setFont(font1)

        self.gridLayout.addWidget(self.btn_9, 7, 5, 1, 2)

        self.radioButton_hexidecimal = QRadioButton(self.frame)
        self.radioButton_hexidecimal.setObjectName(u"radioButton_hexidecimal")

        self.gridLayout.addWidget(self.radioButton_hexidecimal, 4, 3, 1, 1)

        self.radioButton_binary = QRadioButton(self.frame)
        self.radioButton_binary.setObjectName(u"radioButton_binary")

        self.gridLayout.addWidget(self.radioButton_binary, 4, 4, 1, 1)

        self.radioButton_base60 = QRadioButton(self.frame)
        self.radioButton_base60.setObjectName(u"radioButton_base60")

        self.gridLayout.addWidget(self.radioButton_base60, 4, 5, 1, 2)

        self.history_frame = QFrame(self.frame_2)
        self.history_frame.setObjectName(u"history_frame")
        self.history_frame.setGeometry(QRect(710, 0, 280, 430))
        self.history_frame.setFont(font3)
        self.history_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.history_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.history_list = QListWidget(self.history_frame)
        self.history_list.setObjectName(u"history_list")
        self.history_list.setGeometry(QRect(5, 20, 270, 371))
        self.btn_clear_history = QPushButton(self.history_frame)
        self.btn_clear_history.setObjectName(u"btn_clear_history")
        self.btn_clear_history.setGeometry(QRect(10, 390, 30, 30))
        self.btn_clear_history.setIconSize(QSize(24, 24))
        self.menu_frame = QFrame(self.frame_2)
        self.menu_frame.setObjectName(u"menu_frame")
        self.menu_frame.setGeometry(QRect(60, 0, 231, 491))
        self.menu_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.menu_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.btn_standard = QPushButton(self.menu_frame)
        self.btn_standard.setObjectName(u"btn_standard")
        self.btn_standard.setGeometry(QRect(0, 40, 235, 40))
        self.btn_theme = QPushButton(self.menu_frame)
        self.btn_theme.setObjectName(u"btn_theme")
        self.btn_theme.setGeometry(QRect(0, 80, 235, 40))
        self.btn_settings = QPushButton(self.menu_frame)
        self.btn_settings.setObjectName(u"btn_settings")
        self.btn_settings.setGeometry(QRect(0, 120, 235, 40))
        self.btn_about = QPushButton(self.menu_frame)
        self.btn_about.setObjectName(u"btn_about")
        self.btn_about.setGeometry(QRect(0, 160, 235, 40))
        self.btn_menu2 = QPushButton(self.menu_frame)
        self.btn_menu2.setObjectName(u"btn_menu2")
        self.btn_menu2.setGeometry(QRect(8, 9, 30, 30))
        self.btn_menu2.setFont(font2)
        self.btn_menu2.setIcon(icon1)
        self.btn_menu2.setIconSize(QSize(20, 20))
        self.memory_frame = QFrame(self.frame_2)
        self.memory_frame.setObjectName(u"memory_frame")
        self.memory_frame.setGeometry(QRect(290, 529, 380, 290))
        self.memory_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.memory_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.memory_list = QListWidget(self.memory_frame)
        self.memory_list.setObjectName(u"memory_list")
        self.memory_list.setGeometry(QRect(10, 11, 361, 241))
        self.memory_list.setFont(font3)
        self.btn_clear_memory = QPushButton(self.memory_frame)
        self.btn_clear_memory.setObjectName(u"btn_clear_memory")
        self.btn_clear_memory.setGeometry(QRect(20, 250, 30, 30))
        icon2 = QIcon()
        icon2.addFile(u"icons/trash.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_clear_memory.setIcon(icon2)
        self.btn_clear_memory.setIconSize(QSize(24, 24))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1012, 39))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.btn_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.btn_history.setText("")
        self.btn_mplus.setText(QCoreApplication.translate("MainWindow", u"M+", None))
        self.btn_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.btn_dot.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.btn_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.btn_mdown.setText(QCoreApplication.translate("MainWindow", u"M^", None))
        self.btn_clear.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.btn_div.setText(QCoreApplication.translate("MainWindow", u"\u00f7", None))
        self.btn_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.btn_sub.setText(QCoreApplication.translate("MainWindow", u"\u2013\u2014", None))
        self.btn_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.btn_add.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.btn_reciprocal.setText(QCoreApplication.translate("MainWindow", u"\U0000215f\U0001d465", None))
        self.btn_mminus.setText(QCoreApplication.translate("MainWindow", u"M-", None))
        self.radioButton_octal.setText(QCoreApplication.translate("MainWindow", u"Oct", None))
        self.btn_mul.setText(QCoreApplication.translate("MainWindow", u"\u00d7", None))
        self.btn_equal.setText(QCoreApplication.translate("MainWindow", u"=", None))
        self.btn_square.setText(QCoreApplication.translate("MainWindow", u"\U0001d465\U000000b2", None))
        self.btn_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.btn_percent.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Standard", None))
        self.btn_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.btn_sign.setText(QCoreApplication.translate("MainWindow", u"\u00b1", None))
        self.btn_mc.setText(QCoreApplication.translate("MainWindow", u"MC", None))
        self.btn_ms.setText(QCoreApplication.translate("MainWindow", u"MS", None))
        self.btn_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.radioButton_decimal.setText(QCoreApplication.translate("MainWindow", u"Dec", None))
        self.btn_ce.setText(QCoreApplication.translate("MainWindow", u"CE", None))
        self.btn_sqrt.setText(QCoreApplication.translate("MainWindow", u"\u221a", None))
        self.btn_backspace.setText(QCoreApplication.translate("MainWindow", u"\u2190", None))
        self.btn_mr.setText(QCoreApplication.translate("MainWindow", u"MR", None))
        self.btn_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.radioButton_hexidecimal.setText(QCoreApplication.translate("MainWindow", u"Hex", None))
        self.radioButton_binary.setText(QCoreApplication.translate("MainWindow", u"Bin", None))
        self.radioButton_base60.setText(QCoreApplication.translate("MainWindow", u"Sexagesimal", None))
        self.btn_clear_history.setText("")
        self.btn_standard.setText(QCoreApplication.translate("MainWindow", u"Soon", None))
        self.btn_theme.setText(QCoreApplication.translate("MainWindow", u"Soon", None))
        self.btn_settings.setText(QCoreApplication.translate("MainWindow", u"Soon", None))
        self.btn_about.setText(QCoreApplication.translate("MainWindow", u"Soon", None))
        self.btn_clear_memory.setText("")
    # retranslateUi

