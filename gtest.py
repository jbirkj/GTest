import gspread
import time, datetime

try:
    gs = gspread.login('jesperbirkp@gmail.com', 'zxkfdgmtpslbqpzg')
except:
    print('fail')
    sys.exit
sh = gs.open("TempLog1")
wksheet = gs.open("TempLog1").sheet1

#writing to Google sheet
#values = [ datetime.datetime.now(), 'sensor', value1, value2]
#wksheet.append_row(values)


wks = sh.get_worksheet(2)
dateList = wks.col_values(1)     # 0 is first column
temptargetList = wks.col_values(2)

t = datetime.datetime.now()
format = "%d/%m/%Y %H:%M"       #format have is zero padding for numbers
t_now = t.strftime(format)

t1 = dateList[4]
t1

while True:
    t = datetime.datetime.now()
    if t1 == t.strftime(format):
        print("date match")
        break

