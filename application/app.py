from application import modules, utils
import datetime as dt


class App:
    def __init__(self, config: list):
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
        self.config = config
        self.info = ""
        self.info2 = ""
        h = int(self.config[3][0])
        m = int(self.config[3][1])
        s = int(self.config[3][2])
        ms = int(self.config[3][3])
        try:
            assert (0 <= h < 24) & (0 <= m < 60) & (0 <= s < 60) & (0 <= ms < 1000)
        except AssertionError:
            self.info = "时间设置错误"
        else:
            self.info2 = "0"

    def main(self):
        if self.info2 != "":
            stadiumList = ["Badminton Court 1", "Badminton Court 2", 
                                "Badminton Court 3", "Badminton Court 4", 
                                "Badminton Court 5", "Badminton Court 6"]
            periodList = ["15:30 - 16:00", "16:00 - 17:00", "17:00 - 18:00", 
                                "18:00 - 19:00", "19:00 - 20:00", "20:00 - 21:00"]
            weekend = ["Saturday", "Sunday"]
            if dt.datetime.now().strftime("%A") in weekend:
                periodList[0] = "15:00 - 16:00"
            token = self.config[0]
            court = self.queryList["stadiumList"][stadiumList[self.config[1]]]
            courtTime = self.queryList["periodList"][periodList[self.config[2]]]
            bookInfo = [courtTime, court]

            t = self.config[4]
            testTime = modules.ConfigureTime(t)
            testTime.getTimeDelay()
            if testTime.getLocalInterval() < 0:
                self.info = "时间设置错误"
                self.info2 = ""
            else:
                f = modules.Features(token, t)
                self.info, self.info2 = f.bookCourt(bookInfo)
        utils.log(self.info + '\n' + self.info2)
        return self.info, self.info2
