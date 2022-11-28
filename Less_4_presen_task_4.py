import time
from datetime import datetime


n = int(input('Сколько секунд записать в список? '))
timeset = []


def time_now(moment):
    time.sleep(1)
    return datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')

print(f'Подождите {n} секунд')
for moment in range(0, n):
    timeset.append(time_now(moment))
print(timeset)