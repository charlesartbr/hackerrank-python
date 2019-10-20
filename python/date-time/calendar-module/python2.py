import calendar

m, d, y = map(int, raw_input().split())

w = calendar.weekday(y, m, d)

print calendar.day_name[w].upper()
