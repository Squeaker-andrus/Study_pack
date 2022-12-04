text_num = input('Введите вашу цифру ')
def str_in_num(text_num):
    list_of_num = str()
    for i in text_num:
            if i.isdigit() or (i == '-' and text_num[0] == '-') or i == '.':
                list_of_num += i
            else:
                return print(f'{text_num} - некорректное число')
    if sum(map(lambda i: i == '.', list_of_num)) >= 2:
        return print(f'{text_num} - Некорректное число')
    else:
        int_num = str()
        float_num = str()
        for i in list_of_num:
            if i.isdigit() or (i == '-' and list_of_num[0] == '-') or i != '.':
                int_num += i
            elif list_of_num[0] == '.' or (list_of_num[0] == '-' and list_of_num[1] == '.'):
                float_num += '0' + i
            else:
                float_num += i
        return float(float_num) if int_num == () else int(int_num)
print(type(str_in_num(text_num)))
print(str_in_num(text_num))
# Хмм, скипает точку и все выводит в int... думаем...
# Код можно и укоротить, но тогда вообще ничего не понятно будет