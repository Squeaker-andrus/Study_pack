import json, csv
data_dict = {100001: ("Tom", 20),
             100002: ("Matt", 21),
             100003: ("Kevin", 22),
             100004: ("Paul", 23),
             100005: ("Frank", 24),
             100006: ("Garry", 25)
             }
with open("test.json", "w") as file:
    json.dump(data_dict, file)

with open("test.json", "r") as file:
    transport_to: dict = dict(json.load(file))
    with open("table_in_csv.csv", "w", newline="") as new_file:
        creater_file = csv.writer(new_file, delimiter="|")
        creater_file.writerow(["Person1", "Person2", "Person3", "Person4", "Person5", "Person6"])
        creater_file.writerow(transport_to.keys())
        creater_file.writerow(transport_to.values())
        creater_file.writerow(["123-12-12", "123-12-45", "123-12-78", "123-45-12", "123-45-45", "123-45-78"])

# С Excel файлом
# в принципе выполнить задачу можно и я смогу разобратся как(причем без посторонней помощи)
# но неясно с какими плагинами, библиотеками работать
# скачал какой-то плагин, но похоже что зря скачал

