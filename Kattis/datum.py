import datetime
d,m=map(int,input().split())
l=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
o=datetime.date(2009, m, d)
print(l[o.weekday()])