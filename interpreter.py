user = input('enter expression: ').strip()
x, y, z = user.split()
x = float(x)
z = float(z)

if y == '+':
    results = x + z
    print(f'{results: .1f}')
elif y == '-':
    results = x - z
    print(f'{results: .1f}')
elif y == '*':
    results = x * z
    print(f'{results: .1f}')
elif y == '/':
    if z == 0:
        print('error expression')
    results = x / z
    print(f'{results: .1f}')
else:
    print('expression error')
