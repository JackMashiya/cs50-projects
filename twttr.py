user = input('enter word: ')
list1 = ['a','A', 'e', 'E', 'o', 'O', 'u', 'U', 'i', 'I']
new_str = ''
for x in user:
    if x not in list1:
        new_str += x

print(new_str)
