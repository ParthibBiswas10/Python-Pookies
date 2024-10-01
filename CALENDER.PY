# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar
date=input().split()
day=int(date[1])
month=int(date[0])
year=int(date[2])
days=["MONDAY","TUESDAY","WEDNESDAY","THURSDAY","FRIDAY","SATURDAY","SUNDAY"]
ans=calendar.weekday(year,month,day)
print(days[ans])