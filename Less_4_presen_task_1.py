man = {'name': 'Tom', 'age': 23, 'country': 'BY'}
print(man)
new_man = {v:k for k, v in man.items()}
print(new_man)