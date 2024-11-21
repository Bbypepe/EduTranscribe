import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QTimer
from ui.main_window import Ui_MainWindow
from core.audio_processor import get_audio_level

class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_ui()

    def setup_ui(self):
        # Timer to monitor audio levels
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_audio_level)
        self.timer.start(100)  # Update every 100ms

    def update_audio_level(self):
        level = get_audio_level()
        self.ui.audio_meter.setValue(level)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())
