import datetime as dt
year = dt.datetime.now().year
month = dt.datetime.now().month
day = dt.datetime.now().day
hour = dt.datetime.now().hour
minute = dt.datetime.now().minute
second = dt.datetime.now().second

print("오늘은 {}년 {}월 {}일 {}시 {}분 {}초 입니다.".format(year, month, day, hour, minute,second))

