from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import socket

HOST = '192.168.0.10'    # Our IP
PORT = 50007          # The same port as used by the server

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.resize(300, 150)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.btn = QtWidgets.QPushButton(self.centralwidget)
        self.btn.setGeometry(QtCore.QRect(0, 0, 300, 150))

        MainWindow.setCentralWidget(self.centralwidget)

        MainWindow.setWindowTitle("SENDER")
        self.btn.setText('Клик')
        self.btn.setFont(QtGui.QFont("Arial", 32))

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.btn.clicked.connect(self.btn_clicked)
        
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((HOST, PORT))
                

        

    def btn_clicked(self):
        print('btn clicked')
        self.s.sendall(b'next_picture')
        


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())