spisok_slov = ('Олово', 'Комок', 'Ара', 'Клюшка', 'Польша', 'Дорога', 'Увертюра', 'Топот')

print(list(filter(lambda word: word.upper() == word[::-1].upper(), spisok_slov)))