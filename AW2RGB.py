import imghdr
import os
import sys
import PIL
from PIL import Image
import pillow_avif
import glob

from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtWidgets import QMessageBox
from PySide6.QtGui import QIcon

import AW2RGB_ui
from AW2RGB_ui import Ui_MainWindow

class ExampleApp(QtWidgets.QMainWindow, AW2RGB_ui.Ui_MainWindow):
    
    dir0 = ""
    dir1 = ""
    f_list = ""

    def __init__(self):
        super(ExampleApp,self).__init__()
        self.setFixedSize(600, 310)   #fis size window
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_UI()

    def init_UI(self):
        self.ui.dirButton.clicked.connect(self.browse_folder)  # Выполнить функцию browse_folder при нажатии кнопки
        self.ui.pushButton_JPG.clicked.connect(lambda: self.convert("jpg","jpeg"))  # Выполненить функцию конвертации в *jpg при нажатии кнопки
        self.ui.pushButton_PNG.clicked.connect(lambda: self.convert("png","png"))  # Выполнить функцию конвертации в *png при нажатии кнопки     
        self.ui.pushButton_JPGPNG.clicked.connect(self.convertall)  # Выполнить функцию конвертации в *jpg and *png при нажатии кнопки     
        self.ui.dirButton_2.clicked.connect(self.file_select)  # Выполнить функцию browse_folder при нажатии кнопки
        self.ui.pushButton_DELETE.clicked.connect(self.file_delete)  # Выполнить функцию конвертации в *png при нажатии кнопки

    def browse_folder(self):
        self.ui.listView_1.clear()
        self.ui.listView_2.clear()
        try:
            #запрос и смена директории папки dir0
            dirbf0 = QtWidgets.QFileDialog.getExistingDirectory(
               None,
              "Open Directory",
               QtCore.QDir.currentPath(),
               QtWidgets.QFileDialog.ShowDirsOnly | QtWidgets.QFileDialog.DontResolveSymlinks
            )
            os.chdir(dirbf0)
            #запись пути в переменную
            dirbf0 = os.getcwd()+"/"
            dirbf1 = os.getcwd()+"/Sources/"
            self.ui.listView_1.clear()  # На случай, если в списке уже есть элементы
            self.ui.listView_1.addItem(dirbf0)   # добавить файл в listWidget
            ExampleApp.dir0=dirbf0 # передача в глобал
            ExampleApp.dir1=dirbf1 # передача в глобал
        except (OSError, IOError):
                #сообщение об ошибке функции browse_folder - папка не выбрана
                error = QMessageBox()
                error.setWindowTitle("Error")
                error.setIcon(QMessageBox.Warning)
                error.setDefaultButton(QMessageBox.Ok)
                error.setText("Папка не выбрана")
                error.exec() 

    def convert(self,format0,format1):
        if ExampleApp.dir1 != "":
            #список файлов webp и avif
            webpFiles = glob.glob("*.webp")
            avifFiles = glob.glob("*.avif")
            self.ui.listView_2.clear()
            #проверка наличия webp по списку
            if not webpFiles == []:
                #создание папки под сконвертированные img/png, если её нет
                if not os.path.isdir("Sources"):
                    os.mkdir("Sources")
                #создание лог файла
                if not os.path.isfile("log"):
                    log = open("log.txt", "w+")
                    log.writelines("Converted *.webp file to *." + format0 + ":\n")
                #счетчик
                n = 0 
                dird0=ExampleApp.dir0
                dird1=ExampleApp.dir1
                #конвертирование
                for file in webpFiles:
                    #конвертирование файла
                    im = Image.open(file).convert("RGB")
                    #сохранение файла в папку
                    im.save(dird0 + ".".join(file.split(".")[:-1]) + "." + format0, format1)
                    os.replace(dird0 + ".".join(file.split(".")[:-1]) + ".webp", dird1 + ".".join(file.split(".")[:-1]) + ".webp")
                    #запись сконвертированных файлов в лог файл
                    log.writelines(".".join(file.split(".")[:-1]) + ".webp\n")
                    n=n+1
                #вывод счетчика
                log.writelines("Total "+str(n) + " files *.webp converted to *." + format0)
                self.ui.listView_2.addItem("Total " + str(n) + " files *.webp converted to *." + format0)   # добавить в listWidget
                log.close()
            else:
                #проверка наличия *avif по списку
                if not avifFiles == []:
                    #создание папки под сконвертированные img/png, если её нет
                    if not os.path.isdir("Sources"):
                        os.mkdir("Sources")
                    #создание лог файла
                    if not os.path.isfile("log"):
                        log = open("log.txt", "w+")
                        log.writelines("Converted *.avif file to *." + format0 + ":\n")
                    #счетчик
                    m = 0 
                    dird0=ExampleApp.dir0
                    dird1=ExampleApp.dir1
                    #конвертирование
                    for file in avifFiles:
                        #конвертирование файла
                        im = Image.open(file).convert("RGB")
                        #сохранение файла в папку
                        im.save(dird0 + ".".join(file.split(".")[:-1]) + "." + format0, format1)
                        os.replace(dird0 + ".".join(file.split(".")[:-1]) + ".avif", dird1 + ".".join(file.split(".")[:-1]) + ".avif")
                        #запись сконвертированных файлов в лог файл
                        log.writelines(".".join(file.split(".")[:-1]) + ".avif\n")
                        m = m + 1
                    #вывод счетчика
                    log.writelines("Total "+str(m) + " files *.avif converted to *."+format0)
                    self.ui.listView_2.addItem("Total " + str(m) + " files *.avif converted to *." + format0)   # добавить в listWidget
                    log.close()
                else:
                    #сообщение об ошибке  функции convert - не найдены файлы *webp/*avif
                    error = QMessageBox()
                    error.setWindowTitle("Error")
                    error.setIcon(QMessageBox.Warning)
                    error.setDefaultButton(QMessageBox.Ok)
                    error.setText("Файлы *.webp и *.avif не найдены")
                    error.exec()
        else:
            #сообщение об ошибке функции convert - папка не выбрана - browse_folder - пустой
            error = QMessageBox()
            error.setWindowTitle("Error")
            error.setIcon(QMessageBox.Warning)
            error.setDefaultButton(QMessageBox.Ok)
            error.setText("Папка не выбрана")
            error.exec()

    def convertall(self):
        if ExampleApp.dir1 != "":
            #список файлов webp и avif
            webpFiles = glob.glob("*.webp")
            avifFiles = glob.glob("*.avif")
            webavFiles = webpFiles + avifFiles
            self.ui.listView_2.clear()
            #проверка наличия webp по списку
            if not webavFiles == []:
                #создание папки под сконвертированные img/png, если её нет
                if not os.path.isdir("Sources"):
                    os.mkdir("Sources")
                #создание лог файла
                if not os.path.isfile("log"):
                    log = open("log.txt", "w+")
                    log.writelines("Converted *.webp and *.avif files to *.jpg and *.png" + ":\n")
                #счетчик
                n = 0 
                dird0=ExampleApp.dir0
                dird1=ExampleApp.dir1
                #конвертирование
                for file in webavFiles:
                    #конвертирование файла
                    im = Image.open(file).convert("RGB")
                    #сохранение файла в папку
                    im.save(dird0 + ".".join(file.split(".")[:-1]) + "." + "jpg", "jpeg")
                    im.save(dird0 + ".".join(file.split(".")[:-1]) + "." + "png", "png")
                    os.replace(dird0 + ".".join(file.split(".")[:-1]) + ".webp", dird1 + ".".join(file.split(".")[:-1]) + ".webp")
                    #запись сконвертированных файлов в лог файл
                    log.writelines(".".join(file.split(".")[:-1]) + "*.webp\n")
                    n = n + 1
                #вывод счетчика
                log.writelines("Total "+str(n) + " files *.webp and *.avif converted to *.jpg and *.png")
                self.ui.listView_2.addItem("Total " + str(n) + " files *.webp and *.avif converted to *.jpg and *.png")   # добавить в listWidget
                log.close()
            else:
                    #сообщение об ошибке  функции convert - не найдены файлы *webp/*avif
                    error = QMessageBox()
                    error.setWindowTitle("Error")
                    error.setIcon(QMessageBox.Warning)
                    error.setDefaultButton(QMessageBox.Ok)
                    error.setText("Файлы *.webp и *.avif не найдены")
                    error.exec()
        else:
            #сообщение об ошибке функции convert - папка не выбрана - browse_folder - пустой
            error = QMessageBox()
            error.setWindowTitle("Error")
            error.setIcon(QMessageBox.Warning)
            error.setDefaultButton(QMessageBox.Ok)
            error.setText("Папка не выбрана")
            error.exec()

    def file_select(self):
        self.ui.listView_3.clear()
        f_list_l = QtWidgets.QFileDialog.getOpenFileNames(None, 'Select file', '', ("*.webp *.avif"))[0]
        if f_list_l != []:
            f_list_l1 = f_list_l[0] #директория файлов
            n = 0
            ExampleApp.f_list = f_list_l #передача списка файлов в глобал
            n = len(f_list_l)
            self.ui.listView_3.addItem("Selected " + str(n) + " files in " + f_list_l1[: f_list_l1.rfind("/") + 1 ])   # добавить в listWidget
        else:
            #сообщение об ошибке функции file_select - файлы не выбраны
            error = QMessageBox()
            error.setWindowTitle("Error")
            error.setIcon(QMessageBox.Warning)
            error.setDefaultButton(QMessageBox.Ok)
            error.setText("Файлы не выбраны")
            error.exec()
            ExampleApp.f_list = []
            self.ui.listView_3.clear()
    
    def file_delete(self):
        #проверка наличия webp в списке
        f_list_l3 = ExampleApp.f_list
        if f_list_l3 != []:
            k = 0
            #удаление по списку
            for files in f_list_l3:
                os.remove(files)
                k = k + 1
            self.ui.listView_3.addItem("Deleted " + str(k) + " files")   # добавить в listWidget
            ExampleApp.f_list = []
        else:
            #сообщение об ошибке функции convert - папка не выбрана - browse_folder - пустой
            error = QMessageBox()
            error.setWindowTitle("Error")
            error.setIcon(QMessageBox.Warning)
            error.setDefaultButton(QMessageBox.Ok)
            error.setText("Список файлов для удаления пустой")
            error.exec()

def main(): 
    app = QtWidgets.QApplication(sys.argv)
    mainwindow = ExampleApp()
    mainwindow.show()
    sys.exit(app.exec())

main()
