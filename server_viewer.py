import sys
import socket
from PyQt5.Qt import *


HOST = '192.168.0.4'
PORT = 50007

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("SUSCH.VIEWER")

        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)

        self.labelImage = QLabel(self)
        self.labelImage.setStyleSheet(
            "QLabel {background-color: write; border: 1px solid "
            "#0DFFD7; border-radius: 5px;}")
        self.labelImage.setAlignment(Qt.AlignCenter)

        layout = QVBoxLayout(self.centralWidget)
        layout.addWidget(self.labelImage)

        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print(self.s)
        self.s.bind((HOST, PORT))
        print(self.s)
        self.s.listen(1)
        print(self.s)
        self.conn = None
        self.addr = None

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.check_signal)
        self.timer.start(500)


    def openImage(self, image):
        pixmapImage = QPixmap(image)
        pixmapImage = pixmapImage.scaled(
            SCREEN_WIDTH, SCREEN_HEIGHT,
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )
        self.labelImage.setPixmap(pixmapImage)

    def change_image(self):
        global i
        i = (i + 1) % 5
        self.image = f"./images/{i}.jpg"  
        self.openImage(self.image)

    def check_signal(self):
        if not self.conn:
            print('waiting for incoming connection...')
            self.conn, self.addr = self.s.accept()
            print('connection connected!: ', self.conn, ' ', self.addr)

        print(f'Connected by:\n{self.conn}\n{self.addr}\n-----------')
        data: bytes = self.conn.recv(1024)
        if data == b'next_picture':
            print('Received: -> next picture')
            self.change_image()


if __name__ == '__main__':
    global i
    i = 0
    app = QApplication(sys.argv)
    window = MainWindow()
    window.resize(SCREEN_WIDTH, SCREEN_HEIGHT)
    window.show()
    sys.exit(app.exec_())