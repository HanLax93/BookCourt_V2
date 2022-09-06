import argparse
from application import modules, utils
import yaml


def getPars():  # provide a entrance for custom timing time test
    myParser = argparse.ArgumentParser(description='timeSetting')
    myParser.add_argument('-hr', '--hour', type=int, default=12, help='setup hour part')
    myParser.add_argument('-m', '--min', type=int, default=0, help='setup minute part')
    myParser.add_argument('-s', '--sec', type=int, default=0, help='setup second part')
    myParser.add_argument('-d', '--delay', type=int, default=300, help='setup microsecond part')
    a = myParser.parse_args()

    t_h = a.hour
    t_m = a.min
    t_s = a.sec
    t_d = 1 - a.delay/1000
    t = [t_h, t_m, t_s, t_d]
    return t


def getConfig():
    file = open("./config/config.yaml", 'r', encoding="utf-8")
    data = yaml.load(file, Loader=yaml.FullLoader)
    file.close()
    return data


class App:
    def __init__(self, config):
        self.config = config

    def main(self):

        token = self.config['topToken']
        courtTime, court = self.config['topCourtTime'], self.config['topCourt']
        bookInfo = [courtTime, court]

        t = self.config['time']
        testTime = modules.ConfigureTime(t)
        testTime.getTimeDelay()
        if testTime.getLocalInterval() < 0:
            info = "时间设置错误。"
            info2 = "False"
        else:
            f = modules.Features(token, self.config)  # put your token here
            _, ver, _ = f.getPriLogs()
            if ver is not None:
                info, info2 = f.bookCourt(bookInfo)  # put your book info here
            else:
                info, info2 = "Invalid token.", ""
        utils.log(info + '\n' + info2)
        return info, info2
