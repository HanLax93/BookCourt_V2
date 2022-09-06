from PyQt5.QtCore import Qt

from ui.login import Ui_dialog
from ui.func import Ui_MainWindow
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QMainWindow, QApplication
import yaml
import datetime as dt
from application.app import getConfig, App
from application.modules import Features
from application.utils import get_input


class RunThread(QtCore.QThread):
    signal = QtCore.pyqtSignal(list)

    def __init__(self, config):
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
        self.nickname = "login"
        self.token = ""
        memoname = './config/memo.yaml'
        memo = open(memoname, 'r')
        self.memodata = yaml.load(memo, Loader=yaml.FullLoader)
        memo.close()
        self.ui = Ui_dialog(self.memodata)
        self.ui.setupUi(self)
        self.ui.btn_login.clicked.connect(self.login)
        self.setWindowIcon(QtGui.QIcon('src/icon.png'))

        configname = './config/config.yaml'
        config = open(configname, 'r')
        self.config = yaml.load(config, Loader=yaml.FullLoader)
        config.close()

    def login(self):
        self.token = get_input(self.ui.lineEdit_username)
        _, _, self.nickname = Features(self.token, self.config).getPriLogs()
        if self.nickname == "login":
            with open('./config/memo.yaml', 'w') as f:
                self.memodata.update({'topToken': 'Please enter your token.'})
                f.write(yaml.dump(self.memodata, default_flow_style=False))
                f.close()
            self.ui.lineEdit_username.clear()
            self.ui.lineEdit_username.setPlaceholderText('Please check your token.')
        else:
            with open('./config/memo.yaml', 'w') as f:
                self.memodata.update({'topToken': self.token})
                f.write(yaml.dump(self.memodata, default_flow_style=False))
                f.close()
            self.accept()


class Func(QMainWindow):
    def __init__(self, mem):
        super(Func, self).__init__()
        self.setWindowIcon(QtGui.QIcon("src/icon.png"))
        self.thread = None
        self.ui = Ui_MainWindow(mem)
        self.ui.setupUi(self)
        self.ui.btn_sureadd.clicked.connect(self.whatBtnDo)

        self.token = mem['topToken']
        self.nickname = "login"
        self.config = getConfig()
        weekend = ["Saturday", "Sunday"]
        if dt.datetime.now().strftime("%A") in weekend:
            self.config["periodIdList"]["15:x0 - 16:00"] = "22"
        option1 = list(self.config['stadiumIdList'].keys())
        option2 = list(self.config['periodIdList'].keys())
        for i in option1:
            self.ui.comboBox_2.addItem(i)
        for i in option2:
            self.ui.comboBox.addItem(i)

        self.ui.comboBox_2.setCurrentText('Badminton Court 1' if mem['topCourt'] == '' else mem['topCourt'])
        self.ui.comboBox.setCurrentText('15:30 - 16:00' if mem['topCourtTime'] == '' else mem['topCourtTime'])

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Return:
            self.whatBtnDo()

    # 点击按钮触发的函数
    def whatBtnDo(self):
        # TODO: write code here
        t_hour = get_input(self.ui.lineEdit_newname_2)
        t_min = get_input(self.ui.lineEdit_newname)
        t_sec = get_input(self.ui.lineEdit_newname_3)
        delayms = get_input(self.ui.lineEdit_newname_4)
        timing = [t_hour, t_min, t_sec, delayms]
        court = self.ui.comboBox_2.currentText()
        courtTime = self.ui.comboBox.currentText()
        self.config.update({'topToken': self.token, 'topCourt': court, 'topCourtTime': courtTime, 'timing': timing})
        timing = self.config['timing']
        t = [int(timing[0]), int(timing[1]), int(timing[2]), 1 - int(timing[3]) / 1000]
        self.config.update({'time': t})

        fname = './config/memo.yaml'
        mem = open(fname, 'r')
        mem_data = yaml.load(mem, Loader=yaml.FullLoader)
        mem_data.update({'topCourt': court, 'topCourtTime': courtTime, 'timing': timing})
        with open(fname, 'w') as f:
            f.write(yaml.dump(mem_data, default_flow_style=False))
            f.close()

        self.ui.label_9.setText("loading...")

        self.thread = RunThread(self.config)
        self.thread.signal.connect(self.callbacklog)
        self.thread.start()

    def callbacklog(self, msg):
        if msg[1] == "False":
            self.ui.label_9.setText(msg[0])
        elif not msg[1]:
            self.ui.label_9.setText('Invalid token.')
        else:
            self.resize(540, 335)
            self.ui.label_9.setText(msg[0] + '\n' + msg[1])


if __name__ == "__main__":
    window_application = QApplication(sys.argv)
    login_ui = Login()
    if login_ui.exec_() == QDialog.Accepted:
        memo = open('./config/memo.yaml', 'r')
        memo_data = yaml.load(memo, Loader=yaml.FullLoader)
        memo.close()

        main_window = Func(memo_data)
        main_window.setWindowTitle(login_ui.nickname)
        main_window.show()
        sys.exit(window_application.exec())
