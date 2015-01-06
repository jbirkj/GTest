import gspread
import time, datetime

try:
    gs = gspread.login('jesperbirkp@gmail.com', 'zxkfdgmtpslbqpzg')
except:
    print('fail')
    sys.exit
wks = gs.open("TempLog1").sheet1

#writing to Google sheet
#values = [ datetime.datetime.now(), 'sensor', value1, value2]
#wks.append_row(values)

values_list = wkst.col_values(1)

for v in value_list
  print( v )

