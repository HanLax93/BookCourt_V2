import json
import time
from urllib.parse import urlencode
import ntplib
import requests
import datetime as dt

from application.utils import get_key, cryptCBCPkcs7, log


def resolveInfo(params):
    if params['success']:
        return "场地信息如下："
    else:
        return params['errMsg']


class Features:
    def __init__(self, myToken, config=None):  # init with host and token
        queryList = {
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
        self.stadiumIdList = queryList["stadiumList"]
        self.periodIdList = queryList["periodList"]
        self.token = myToken
        self.headers = {
            "Host": "tyb.qingyou.ren",
            "User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; SM-G977N Build/LMY48Z; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.136 Mobile Safari/537.36 MMWEBID/4347 MicroMessenger/8.0.22.2140(0x280016F7) WeChat/arm32 Weixin NetType/WIFI Language/zh_CN ABI/arm32 MiniProgramEnv/android",
            "Charset": "utf-8",
            "Accept-Encoding": "gzip, deflate"}
        self.host = "https://tyb.qingyou.ren"
        if config is not None:
            self.time = config

    # def cancelCourt(self):  # you can try to cancel the booking with this function
    #     data, _, _ = self.getPriLogs()
    #     stadiumId = data['data'][0]['id']  # the id of the latest court booking
    #     params = {"logId": str(stadiumId)}  # request params
    #     params = json.dumps(params)

    #     url = self.host + "/user/cancel"  # url to which cancel request post
    #     headers = self.headers
    #     headers.update({"token": self.token, "Content-Type": "application/x-www-form-urlencoded"})  # request headers

    #     s = requests.post(url, params, headers=headers)  # response information
    #     return s

    def bookBadminton(self, p):  # try to book a Badminton court
        today = '{:%Y-%m-%d}'.format(dt.datetime.now())  # the date today
        # request params including the id and the time you want to book
        params = {"periodId": p[0], "date": today, "stadiumId": p[1]}
        params = json.dumps(params)
        log(params)
        url = self.host + "/user/book"  # url to which book request post
        # time and signature time when request sends
        timestamp, timestampSignature = ConfigureTime(self.time).getTimeVerify()
        headers = self.headers
        headers.update({"token": self.token, "Resultjson": timestamp, "Content-Type": "application/json",
                        "Resultjsonsignature": timestampSignature})  # request headers
        s = requests.post(url, params, headers=headers)  # response information including the result of booking
        return s.json()

    def getPriLogs(self,):  # get the latest booking info
        # limit param means only return the latest booking info
        nickname = "login"
        infoSum = None
        data = {"containCanceled": "false", "desc": "true", "limit": "1", "offset": "0"}
        data = json.dumps(data)
        url = self.host + "/user/getPriLogs"  # url to which query request post

        headers = self.headers
        # request headers
        headers.update({"token": self.token, "Content-Type": "application/json"})

        try:
            s = requests.post(url, data, headers=headers).json()
        except Exception:
            s = None
        else:
            try:
                myData = s['data']
            except KeyError:
                pass
            else:
                court = get_key(self.stadiumIdList, str(myData[0]["stadiumId"]))[0]
                infoSum = court + '\n' + myData[0]['period'] + '\n' + myData[0]['date']
                nickname = myData[0]['nickName']
        return s, infoSum, nickname

    def bookCourt(self, params):  # countdown and then book
        info = {}
        postTime = None
        _, _, _, t_delay = self.time  # get delay microseconds
        ct = ConfigureTime(self.time)
        ct.countTo2()  # countdown to last 2 min

        flag = True
        # countdown to the timing time
        while flag:
            time.sleep(0.989)
            # print(getLocalInterval(rt, de))
            if ct.getLocalInterval() <= 3:
                while flag:
                    if ct.getLocalInterval() <= t_delay:
                        postTime = time.time()
                        # print("数据发送时间：", time.time()+ct.delay)
                        info = self.bookBadminton(params)
                        # print("数据返回时间：", time.time()+ct.delay)
                        # print(info)
                        flag = False

        # print the latest booked court after 5 sec
        time.sleep(5)
        _, ret2, _ = self.getPriLogs()

        if not info['success']:
            ret1 = info['errMsg']
            ret2 = ""
        else:
            ntpTime, _ = ct.getNtpTime()
            relTime = ntpTime.tx_time + ntpTime.delay / 2 - (time.time() - postTime)
            ret1 = "提交时间:\n" + ct.styledTime(relTime, False) + '\n' + resolveInfo(info)
        return ret1, ret2
    

class ConfigureTime:
    def __init__(self, mytime):  # init the delay with 0 and the timing time
        self.delay = 0
        self.time = mytime
        self.timingTime = self.setTime()

    def countTo2(self):  # countdown to last 2 min
        self.getTimeDelay()
        flag = True
        while flag:
            if self.getLocalInterval() > 120:
                time.sleep(60)
            else:
                flag = False
        self.getTimeDelay()

    def getTimeDelay(self):  # get delay between local time and server time
        timeDelay = 0

        # take the average of ten items as delay
        for i in range(10):
            ntpClient = ntplib.NTPClient()
            times = ntpClient.request("edu.ntp.org.cn", version=2)  # get the server time from the china education web

            timeDelay += times.tx_time + times.delay / 2 - time.time()

        self.delay = timeDelay / 10
        return self.delay

    def getInterval(self):  # get time interval between server time and timing time
        ntpClient = ntplib.NTPClient()
        interval = self.timingTime - ntpClient.request("edu.ntp.org.cn", version=2, timeout=3).tx_time
        return interval

    def getLocalInterval(self):  # get the time interval between local time and timing time but within delay
        localTimestamp = time.time()
        interval = self.timingTime - localTimestamp - self.delay
        return interval

    def setTime(self):  # get the timestamp of the timing time
        th, tm, ts, _ = self.time

        today = "{:%Y-%m-%d}".format(dt.datetime.now())

        tm = tm + 1 if ts == 59 else tm
        th = th + 1 if tm == 60 else th
        ts = ts + 1
        ts = 0 if ts == 60 else ts
        tm = 0 if tm == 60 else tm

        ret_hour = str(th)
        ret_min = '0' + str(tm) if tm <= 9 else str(tm)
        ret_sec = '0' + str(ts) if ts <= 9 else str(ts)

        ret = today + ' ' + ret_hour + ':' + ret_min + ':' + ret_sec
        ret = time.strptime(ret, '%Y-%m-%d %H:%M:%S')
        return time.mktime(ret)

    def styledTime(self, t, local=True):
        if local:
            t = t + self.delay
        tmp = time.localtime(t)
        tmp = time.strftime('%Y-%m-%d %H:%M:%S', tmp)

        st = tmp + ' ' + str(round(t % 1 * 1000))

        return st

    def getTimeVerify(self):  # get signature value of timestamp when request sends
        _, _, _, t_ms = self.time
        key = "6f00cd9cade84e52"
        iv = "25d82196341548ef"
        cryptor = cryptCBCPkcs7(key, iv)

        TS_hms = str(round(self.timingTime - 1))
        TS_ms = round(1000 - t_ms*1000)
        if TS_ms < 10:
            TS = TS_hms + "00" + str(TS_ms)
        elif TS_ms < 100:
            TS = TS_hms + '0' + str(TS_ms)
        else:
            TS = TS_hms + str(TS_ms)
        TSS = cryptor.encrypt(TS).decode()
        return TS, TSS

    @staticmethod
    def getNtpTime():  # just get the server time
        ntpClient = ntplib.NTPClient()
        times = ntpClient.request("edu.ntp.org.cn", version=2)

        localTime = time.localtime(times.tx_time)
        localTime = time.strftime("%Y-%m-%d %H:%M:%S", localTime)
        return times, localTime + str(times.tx_time % 1)
