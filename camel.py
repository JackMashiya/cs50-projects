user = input('camelCase: ')
def main(word):
    snake = ''
    for x in word:
        if x.isupper():
            snake += '_' + x.lower()
        else:
            snake += x
    return snake

print(main(user))


