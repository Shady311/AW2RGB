import imghdr
import os
from PIL import Image
import glob
#импорт PySide6
from PySide6 import QtCore, QtWidgets
from PySide6.QtWidgets import QMessageBox
#код
try:
    #запрос и смена директории в патч
    app = QtWidgets.QApplication([])
    dir = QtWidgets.QFileDialog.getExistingDirectory(
       None,
      ("Open Directory"),
       QtCore.QDir.currentPath(),
       QtWidgets.QFileDialog.ShowDirsOnly | QtWidgets.QFileDialog.DontResolveSymlinks
    )
    os.chdir(dir)
    #запись пути в переменную
    dir = os.getcwd()+"/"
    dir1 = os.getcwd()+"/WEBP/"
    test = QtCore.QDir.currentPath()
    #список webp
    webpFiles = glob.glob("*.webp")
    #проверка наличия webp по списку
    if not webpFiles == []:
        #создание папки под сконвертированные IMG
        if not os.path.isdir("WEBP"):
             os.mkdir("WEBP")
        #создание лог файла
        if not os.path.isfile("log"):
            log = open("log.txt", "w+")
            log.writelines("Converted to .jpg:\n")
        #счетчик
        n = 0 
        #конверт
        for file in webpFiles:
            #конвертирование файла
            im = Image.open(file).convert("RGB")
            #сохранение файла в папку
            im.save(dir+file.split(".")[0]+".jpg", "jpeg")
            os.replace(dir+file.split(".")[0]+".webp", dir1+file.split(".")[0]+".webp")
            #запись сконвертированных файлов в лог файл
            log.writelines(file.split(".")[0]+".webp\n")
            n=n+1
        #вывод счетчика
        log.writelines("Total "+str(n)+" files")
        log.close()
    else:
        #сообщение об ошибке 1
        error = QMessageBox()
        error.setWindowTitle("Error")
        error.setIcon(QMessageBox.Warning)
        error.setDefaultButton(QMessageBox.Ok)
        error.setText("Файлы *.webp не найдены")
        error.exec()
except (OSError, IOError):
        #сообщение об ошибке 2
        error = QMessageBox()
        error.setWindowTitle("Error")
        error.setIcon(QMessageBox.Warning)
        error.setDefaultButton(QMessageBox.Ok)
        error.setText("Папка не выбрана")
        error.exec()