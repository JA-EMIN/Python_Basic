import datetime
import threading

# dt = datetime.date(1999,11,10)
# # print(dt)
# # print(dt.year, dt.month, dt.day, sep=',')
# #
# # tm = datetime.time(11,10,15)
# # print(tm)
# # print(tm.hour, tm.minute, tm.second, sep=',')
# #
# # dttm = datetime.datetime.now()
# # print(dttm)
# #
# # dttm = datetime.datetime(1998,1,10,12,13,14)
# # print(dttm)
# # print(dttm.year, dttm.month, dttm.day, dttm.hour, dttm.minute, dttm.second, sep=',')
# #
# # s = dttm.strftime('%Y-%m-%d %p)

iTime = input("현재 시간을 입력하세요 ex) 2019-11-11 11:11:11 : ")
currentTime = datetime.datetime.now()
iTime = datetime.datetime.strptime(iTime, "%Y-%m-%d %H:%M:%S")


def countDown():
        t = threading.Timer(0.5, countDown)
        t.start()
        timeDelta = iTime - datetime.datetime.now()
        gap = timeDelta.total_seconds()

        if 10 < gap <= 30:
            print(gap)
        elif gap <= 10.0:
            t.cancel()

countDown()