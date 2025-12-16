import sys
import cv2
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton
from PySide6.QtCore import QTimer,Qt
from PySide6.QtGui import QImage, QPixmap

class CameraApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("外置摄像头图传界面")
        self.setGeometry(100, 100, 640, 480)

        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)

        self.label = QLabel()
        self.label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label)

        self.button = QPushButton("打开/关闭摄像头")
        self.button.clicked.connect(self.toggle_camera)
        layout.addWidget(self.button)

        self.setCentralWidget(central_widget)

        self.cap = cv2.VideoCapture(0)

        if not self.cap.isOpened():
            print("无法打开外置摄像头，请检查连接")
            self.cap = None
        else:
            print("成功打开外置摄像头")

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)

        self.is_camera_running = False

    def toggle_camera(self):

        if self.is_camera_running:
            self.timer.stop()
            if self.cap:
                self.cap.release()
            self.is_camera_running = False
            self.button.setText("打开摄像头")
        else:
            if self.cap:
                self.timer.start(30)
                self.is_camera_running = True
                self.button.setText("关闭摄像头")
            else:
                print("摄像头初始化失败")

    def update_frame(self):

        if self.cap and self.cap.isOpened():
            ret, frame = self.cap.read()
            if ret:

                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                height, width, channels = frame.shape
                bytes_per_line = channels * width

                q_img = QImage(frame.data, width, height, bytes_per_line, QImage.Format_RGB888)

                pixmap = QPixmap.fromImage(q_img)
                self.label.setPixmap(pixmap.scaled(self.label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))

    def closeEvent(self, event):

        if self.cap:
            self.cap.release()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CameraApp()
    window.show()
    sys.exit(app.exec())
