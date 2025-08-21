def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    length = len(s)
    numbers = []
    if not 2 <= length <= 6:
        return False

    if not s[0].isalpha() or not s[1].isalpha():
        return False

    if not s.isalnum():
        return False

    for x in s:
        if x.isnumeric():
            numbers.append(x)
    if numbers and numbers[0] == '0':
        return False

    for i in range(len(s) - 1):
        if s[i].isnumeric() and s[i + 1].isalpha():
            return False
    return True

main()

