
user = input('enter file name: ').lower().strip()
if '.' not in user:
    print('application/octet-stream')
else:
    if user.endswith('.jpg'):
        print('image/jpeg')
    elif user.endswith('.jpeg'):
        print('image/jpeg')
    elif user.endswith('.zip'):
        print('application/zip')
    elif user.endswith('.png'):
        print('image/png')
    elif user.endswith('.pdf'):
        print('application/pdf')
    elif user.endswith('.txt'):
        print('text/plain')
    elif user.endswith('.gif'):
        print('image/gif')
    else:
        print('application/octet-stream')

