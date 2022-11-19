# Первый вариант


# def how_much(num_list, n):
#     how_much_list = []
#     for i in num_list:
#         if i == n:
#             how_much_list.append(n)
#
#     return len(how_much_list)
#
#
# numbers_list = [1, 4, 5, 2, 4, 3, 4, 2, 1, 3]
# search_n = 4
# print(f'Данных чисел в списке {how_much(numbers_list, search_n)}')


# Второй вариант


def how_much(num_dict, n):
    num_much = 0
    for i in num_dict.values():
        if i == n:
            num_much += 1
    return num_much

numbers_dict = {'num1' : 1,
                'num2' : 4,
                'num3' : 5,
                'num4' : 2,
                'num5' : 4,
                'num6' : 3,
                'num7' : 4,
                'num8' : 2,
                'num9' : 1,
                'num10' : 3
                }
search_n = 4
print(f'Данных чисел в списке {how_much(numbers_dict, search_n)}')