import random

def main():
    level = get_level()
    score = 0

    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        correct = x + y
        tries = 0
        while tries < 3:
            try:
                answer = int(input(f"{x} + {y} = "))
            except ValueError:
                print("EEE")
                tries += 1
                continue

            if answer == correct:
                score += 1
                break
            else:
                print("EEE")
                tries += 1

        if tries == 3:
            print(correct)

    print(f"Score: {score}/10")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
        except ValueError:
            pass
        continue


def generate_integer(level):
    if level not in [1, 2, 3]:
        raise ValueError("Level must be 1, 2, or 3.")

    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    else:
        return random.randint(100, 999)

main()
