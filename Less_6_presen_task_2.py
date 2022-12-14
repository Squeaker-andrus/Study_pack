a = input('После ввода текста нажмите Enter ')
b = input('После ввода текста нажмите Enter ')
c = input('После ввода текста нажмите Enter ')
d = input('После ввода текста нажмите Enter ')

test_text = open('test_text.txt', 'w')
test_text.write(f'{a}\n{b}\n')
test_text.close()

test_text = open('test_text.txt', 'a')
test_text.write(f'{c}\n{d}\n')
test_text.close()
