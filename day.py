from datetime import date

today = date.today()
print("Today`s date")

from datetime import date

today = date.today()
d1 = today.strftime("sunday")
print("d1 =", d1)
d2 = today.strftime("Monday")
print("d2 =",d2)
d3 = today.strftime("Tuesday")
print("d3 =",d3)

from datetime import datetime

now = datetime.now()
print("now =", now)

dt_string = now.strftime( )
print("date and time")

