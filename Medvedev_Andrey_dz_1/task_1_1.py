duration = int(input("duration: "))
day_d = duration // 86400
hour_d = (duration // 3600) % 24
min_d = (duration // 60) % 60
sec_d = duration % 60

if min_d >= 10:
    min_d = str(min_d)
else:
    min_d = str('0' + str(min_d))
if sec_d < 10:
    sec_d = str('0' + str(sec_d))
else:
    sec_d = str(sec_d)

print(str(day_d) + " дней " + str(hour_d) + " часов " + str(min_d) + " минут " + str(sec_d) + " секунд ")
