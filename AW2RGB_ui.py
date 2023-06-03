# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AW2RGB_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QListWidget,
    QListWidgetItem, QMainWindow, QPushButton, QSizePolicy,
    QToolButton, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(600, 310)
        icon = QIcon()
        icon.addFile(u"AW2RGB.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"background-color: rgb(229, 229, 229);\n"
"font: 900 12pt \"Segoe UI\";\n"
"border-radius: 5px; ")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.dir_change = QLabel(self.centralwidget)
        self.dir_change.setObjectName(u"dir_change")
        self.dir_change.setGeometry(QRect(20, 50, 281, 21))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        self.dir_change.setFont(font)
        self.dir_change.setLayoutDirection(Qt.LeftToRight)
        self.dir_change.setStyleSheet(u"\n"
"color: rgb(0, 0, 0);\n"
"font: 700 10pt \"Segoe UI\";")
        self.dir_change.setTextFormat(Qt.AutoText)
        self.dir_change.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.pushButton_JPG = QPushButton(self.centralwidget)
        self.pushButton_JPG.setObjectName(u"pushButton_JPG")
        self.pushButton_JPG.setGeometry(QRect(310, 150, 71, 41))
        self.pushButton_JPG.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(249, 170, 51);\n"
"color: rgb(40, 47, 57);\n"
"font: 900 10pt \"Segoe UI\";\n"
"border-radius: 9px; \n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(35, 47, 52);\n"
"color: rgb(255, 255, 255);\n"
"font: 900 10pt \"Segoe UI\";\n"
"border-radius: 9px; \n"
"}")
        self.pushButton_JPG.setAutoDefault(False)
        self.pushButton_JPG.setFlat(False)
        self.pushButton_PNG = QPushButton(self.centralwidget)
        self.pushButton_PNG.setObjectName(u"pushButton_PNG")
        self.pushButton_PNG.setGeometry(QRect(390, 150, 71, 41))
        self.pushButton_PNG.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(249, 170, 51);\n"
"color: rgb(40, 47, 57);\n"
"font: 900 10pt \"Segoe UI\";\n"
"border-radius: 9px; \n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(35, 47, 52);\n"
"color: rgb(255, 255, 255);\n"
"font: 900 10pt \"Segoe UI\";\n"
"border-radius: 9px; \n"
"}")
        self.dirButton = QToolButton(self.centralwidget)
        self.dirButton.setObjectName(u"dirButton")
        self.dirButton.setGeometry(QRect(310, 50, 271, 21))
        self.dirButton.setStyleSheet(u"QToolButton{\n"
"background-color: rgb(249, 170, 51);\n"
"color: rgb(40, 47, 57);\n"
"font: 900 12pt \"Segoe UI\";\n"
"border-radius: 9px; \n"
"}\n"
"QToolButton:pressed{\n"
"background-color: rgb(35, 47, 52);\n"
"color: rgb(255, 255, 255);\n"
"font: 900 12pt \"Segoe UI\";\n"
"border-radius: 9px; \n"
"}")
        self.listView_1 = QListWidget(self.centralwidget)
        self.listView_1.setObjectName(u"listView_1")
        self.listView_1.setGeometry(QRect(20, 80, 561, 41))
        self.listView_1.setStyleSheet(u"background-color: rgb(74, 101, 114);\n"
"color: rgb(255, 255, 255);\n"
"font: 8pt \"Segoe UI\";\n"
"border: none;")
        self.listView_1.setWordWrap(True)
        self.listView_2 = QListWidget(self.centralwidget)
        self.listView_2.setObjectName(u"listView_2")
        self.listView_2.setGeometry(QRect(20, 150, 281, 41))
        self.listView_2.setStyleSheet(u"background-color: rgb(74, 101, 114);\n"
"color: rgb(255, 255, 255);\n"
"font: 8pt \"Segoe UI\";\n"
"border: none;")
        self.listView_2.setWordWrap(True)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 0, 561, 41))
        self.label.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 900 18pt \"Segoe UI\";")
        self.label.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 125, 271, 21))
        self.label_2.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 700 10pt \"Segoe UI\";")
        self.label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.dir_change_2 = QLabel(self.centralwidget)
        self.dir_change_2.setObjectName(u"dir_change_2")
        self.dir_change_2.setGeometry(QRect(20, 210, 281, 21))
        self.dir_change_2.setFont(font)
        self.dir_change_2.setLayoutDirection(Qt.LeftToRight)
        self.dir_change_2.setStyleSheet(u"\n"
"color: rgb(0, 0, 0);\n"
"font: 700 10pt \"Segoe UI\";")
        self.dir_change_2.setTextFormat(Qt.AutoText)
        self.dir_change_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.dirButton_2 = QToolButton(self.centralwidget)
        self.dirButton_2.setObjectName(u"dirButton_2")
        self.dirButton_2.setGeometry(QRect(310, 210, 271, 21))
        self.dirButton_2.setStyleSheet(u"QToolButton{\n"
"background-color: rgb(249, 170, 51);\n"
"color: rgb(40, 47, 57);\n"
"font: 900 12pt \"Segoe UI\";\n"
"border-radius: 9px; \n"
"}\n"
"QToolButton:pressed{\n"
"background-color: rgb(35, 47, 52);\n"
"color: rgb(255, 255, 255);\n"
"font: 900 12pt \"Segoe UI\";\n"
"border-radius: 9px; \n"
"}")
        self.listView_3 = QListWidget(self.centralwidget)
        self.listView_3.setObjectName(u"listView_3")
        self.listView_3.setGeometry(QRect(20, 240, 401, 51))
        self.listView_3.setStyleSheet(u"background-color: rgb(74, 101, 114);\n"
"color: rgb(255, 255, 255);\n"
"font: 8pt \"Segoe UI\";\n"
"border: none;")
        self.listView_3.setWordWrap(True)
        self.pushButton_DELETE = QPushButton(self.centralwidget)
        self.pushButton_DELETE.setObjectName(u"pushButton_DELETE")
        self.pushButton_DELETE.setGeometry(QRect(430, 240, 151, 51))
        self.pushButton_DELETE.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(249, 170, 51);\n"
"color: rgb(40, 47, 57);\n"
"font: 900 10pt \"Segoe UI\";\n"
"border-radius: 9px; \n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(35, 47, 52);\n"
"color: rgb(255, 255, 255);\n"
"font: 900 10pt \"Segoe UI\";\n"
"border-radius: 9px; \n"
"}")
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(20, 200, 561, 3))
        self.line.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"border-radius: 1px; ")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.pushButton_JPGPNG = QPushButton(self.centralwidget)
        self.pushButton_JPGPNG.setObjectName(u"pushButton_JPGPNG")
        self.pushButton_JPGPNG.setGeometry(QRect(470, 150, 111, 41))
        self.pushButton_JPGPNG.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(249, 170, 51);\n"
"color: rgb(40, 47, 57);\n"
"font: 900 10pt \"Segoe UI\";\n"
"border-radius: 9px; \n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(35, 47, 52);\n"
"color: rgb(255, 255, 255);\n"
"font: 900 10pt \"Segoe UI\";\n"
"border-radius: 9px; \n"
"}")
        self.pushButton_JPGPNG.setAutoRepeat(False)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.pushButton_JPG.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"AW2RGB", None))
        self.dir_change.setText(QCoreApplication.translate("MainWindow", u"Change directory *.avif/*.webp files:", None))
        self.pushButton_JPG.setText(QCoreApplication.translate("MainWindow", u"*.jpg", None))
        self.pushButton_PNG.setText(QCoreApplication.translate("MainWindow", u"*.png", None))
        self.dirButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"AW2RGB", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Convert log:", None))
        self.dir_change_2.setText(QCoreApplication.translate("MainWindow", u"Select wrecked *.avif/*.webp files:", None))
        self.dirButton_2.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.pushButton_DELETE.setText(QCoreApplication.translate("MainWindow", u"Delete selected file", None))
        self.pushButton_JPGPNG.setText(QCoreApplication.translate("MainWindow", u"*.jpg and *.png", None))
    # retranslateUi

