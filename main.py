from PyQt5.QtCore import Qt
import json
from ui.login import Ui_dialog
from ui.func import Ui_MainWindow
import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QDialog, QMainWindow, QApplication
from application.app import App
from application.modules import Features
from application.utils import get_input


class RunThread(QtCore.QThread):
    signal = QtCore.pyqtSignal(list)
    
    def __init__(self, config: list):
        super(RunThread, self).__init__()
        self.config = config

    def run(self):
        a = App(self.config)
        t1, t2 = a.main()
        ret = [t1, t2]
        self.signal.emit(ret)


class Login(QDialog):
    def __init__(self):
        super(Login, self).__init__()
        with open("./config/config.json", 'r') as f:
            tmp = json.load(f)
            f.close()
        config = tmp["config"]
        topToken = config[0]
        self.topCourt = config[1]
        self.topCourtTime = config[2]
        self.timing = config[3]
        
        self.nickname = "login"
        self.token = ""
        self.ui = Ui_dialog()
        self.ui.setupUi(self)
        self.ui.lineEdit_username.setPlaceholderText(topToken)
        self.ui.btn_login.clicked.connect(self.login)

    def login(self):
        token = get_input(self.ui.lineEdit_username)
        _, _, self.nickname = Features(token).getPriLogs()
        if self.nickname == "login":
            self.ui.lineEdit_username.clear()
            self.ui.lineEdit_username.setPlaceholderText('Please check your token')
        else:
            if self.nickname == "孙泽":
                self.nickname = "狗泽"
            self.token = token
            self.accept()


class Func(QMainWindow):
    def __init__(self):
        super(Func, self).__init__()
        self.queryList = {
            "stadiumList":{
                "Badminton Court 1": "5",
                "Badminton Court 2": "6",
                "Badminton Court 3": "7",
                "Badminton Court 4": "8",
                "Badminton Court 5": "13",
                "Badminton Court 6": "14"
            },
            "periodList":{
                "15:30 - 16:00":  "21",
                "15:00 - 16:00":  "22",
                "16:00 - 17:00": "2",
                "17:00 - 18:00": "3",
                "18:00 - 19:00": "4",
                "19:00 - 20:00": "5",
                "20:00 - 21:00": "6"
            }
        }
        self.thread = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_sureadd.clicked.connect(self.whatBtnDo)

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Return:
            self.whatBtnDo()

    # 点击按钮触发的函数
    def whatBtnDo(self):
        # TODO: write code here
        self.ui.label_9.setText("loading...")
        config = self.configParams()
        saveConfig = config[0:4]
        with open("./config/config.json", 'w') as f:
            json.dump({"config": saveConfig}, f)
            f.close()
        if self.thread is not None:
            self.thread.quit()
            if self.thread.isRunning():
                self.thread.terminate()
        self.thread = RunThread(config)
        self.thread.signal.connect(self.callbacklog)
        self.thread.start()

    def configParams(self):
        t_hour = get_input(self.ui.lineEdit_newname_2)
        t_min = get_input(self.ui.lineEdit_newname)
        t_sec = get_input(self.ui.lineEdit_newname_3)
        delayms = get_input(self.ui.lineEdit_newname_4)
        timing = [t_hour, t_min, t_sec, delayms]
        court = self.ui.comboBox_2.currentIndex()
        courtTime = self.ui.comboBox.currentIndex()
        t = [int(timing[0]), int(timing[1]), int(timing[2]), 1 - int(timing[3]) / 1000]
        config = [self.token, court, courtTime, timing, t, self.nickname]
        return config

    def callbacklog(self, msg):
        self.ui.label_9.setText(msg[0] + '\n' + msg[1])


if __name__ == "__main__":
    window_application = QApplication(sys.argv)
    login_ui = Login()
    if login_ui.exec_() == QDialog.Accepted:
        main_window = Func()
        config = [login_ui.token, login_ui.topCourt, login_ui.topCourtTime, login_ui.timing, login_ui.nickname]
        main_window.token = config[0]
        main_window.nickname = config[4]
        main_window.ui.comboBox_2.setCurrentIndex(config[1])
        main_window.ui.comboBox.setCurrentIndex(config[2])
        main_window.ui.lineEdit_newname_2.setPlaceholderText(config[3][0])
        main_window.ui.lineEdit_newname.setPlaceholderText(config[3][1])
        main_window.ui.lineEdit_newname_3.setPlaceholderText(config[3][2])
        main_window.ui.lineEdit_newname_4.setPlaceholderText(config[3][3])
        main_window.setWindowTitle(config[4])
        main_window.show()
        sys.exit(window_application.exec())
