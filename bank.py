word = 'hello'
user = input('Greeting: ').strip().lower()
if user.startswith(word):
    print(f'${0}')
elif user.startswith('h'):
    print(f'${20}')
else:
    print(f'${100}')

