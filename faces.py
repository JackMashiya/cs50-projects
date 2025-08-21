def convert(text):
        final = None
        if ':)' in text or ':(' in text:
                final = text.replace(':)', '🙂').replace(':(', '🙁')
        return final

def main():
    user = input('enter text please: ')
    print(convert(user))

main()


