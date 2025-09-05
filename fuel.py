


def convert(fraction):

    try:
        x, y = fraction.split("/")
        x = int(x)
        y = int(y)
    except ValueError:
        raise ValueError("X and Y must be integers")

    if y == 0:
        raise ZeroDivisionError("Denominator cannot be zero")
    if x > y:
        raise ValueError("Numerator cannot be greater than denominator")

    percentage = round((x / y) * 100)
    return percentage


def gauge(percentage: int) -> str:

    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


def main():
    fraction = input("Fraction: ")
    try:
        percentage = convert(fraction)
        print(gauge(percentage))
    except (ValueError, ZeroDivisionError):
        print("Error")


if __name__ == "__main__":
    main()
