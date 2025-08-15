
def main():
    while True:
        try:
            user = input('enter fraction: ')
            x, y = user.split('/')
            x = int(x)
            y = int(y)
            if x < 0 or x > y or y <= 0:
                raise ValueError

            percentage = round((x / y) * 100)

            if percentage <= 1:
                print('E')
            elif percentage >= 99:
                print('F')
            else:
                print(f'{percentage}%')
            break
        except (ValueError, ZeroDivisionError):
            continue


main()
