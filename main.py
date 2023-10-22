import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QDialog, QMessageBox
import ydownload

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True) #enable highdpi scaling
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True) #use highdpi icons

class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow,self).__init__()
        loadUi("interface.ui",self)
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setWindowTitle("Youtube Dowloader")
        self.pushButton.clicked.connect(self.dowload)

    # Function for feedback
    def showmsg(self, type):
        if type == "information":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Information")
            msg.setText("Download Completed.")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
        elif type == "warning":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Warning")
            msg.setText("Please Enter Valid Information.")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_() 
        self.lineEdit.clear()

    # Main function that controls the url and the download functions
    def dowload(self):
        try:
            url = self.lineEdit.text()
            if self.checkBox.isChecked() and self.checkBox_2.isChecked():
                self.mp4playlistdowload(url)
                self.checkBox.setChecked(False)
                self.checkBox_2.setChecked(False)
                self.showmsg("information")

            elif self.checkBox_2.isChecked() and self.checkBox_3.isChecked():
                self.mp3playlistdowload(url)
                self.checkBox_2.setChecked(False)
                self.checkBox_3.setChecked(False)
                self.showmsg("information")
                self.lineEdit.clear()

            elif self.checkBox.isChecked():
                self.mp4dowload(url)
                self.checkBox.setChecked(False)
                self.showmsg("information")
                self.lineEdit.clear()

            elif self.checkBox_2.isChecked():
                self.mp3dowload(url)
                self.checkBox_2.setChecked(False)
                self.showmsg("information")

            else:
                self.showmsg("warning")
        except:
            self.showmsg("warning")

    # Functions that use module for downloading
    def mp3dowload(self, url):
        control = ydownload.dowload_mp3(url)
    
    def mp3playlistdowload(self, url):
        control = ydownload.dowload_mp3_playlist(url)
    
    def mp4dowload(self, url):
        control = ydownload.dowload_mp4(url)

    def mp4playlistdowload(self, url):
        control = ydownload.dowload_mp4_playlist(url)

app = QtWidgets.QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
win = MainWindow()
widget.addWidget(win)
widget.setFixedSize(800, 500)
widget.setWindowTitle("Youtube Dowloader")
widget.show()

sys.exit(app.exec_())