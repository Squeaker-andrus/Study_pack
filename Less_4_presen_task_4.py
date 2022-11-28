from datetime import datetime


n = int(input('Сколько секунд записать в список? '))
timeset = []


def time_now(moment, n):
    if n == [None] or datetime.now() - n == 1:
        return datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')


for moment in range(0, n):
    timeset.append(time_now(moment, timeset[]))
print(timeset)