import datetime

birth=datetime.date(1992,8,13)
print("My birthday is at", birth)
print("year:", birth.year)
print("month:",birth.month)
print("day:", birth.day)
print("weekday:",birth.weekday())

nextbirth=datetime.date(2020,8,13)
tday=datetime.date.today()
print("until the next birthday",nextbirth-tday, "\n")


import calendar
cal= calendar.month(2017,5)

print( cal)

one_day = datetime.timedelta(days = 1)

tday=datetime.datetime(2019,11,1,10,57)
yesterday=tday-one_day
print("yesterday", yesterday)

two_day= datetime.timedelta(days = 2)

twodays=tday+two_day
print(twodays)

three=datetime.timedelta(days=3)
threedays=yesterday-three
print(threedays)