import random

def prompt(msg):
    while True:
        try:
            value = int(input(msg))
            if value > 0:
                return value
        except ValueError:
            pass

def main():
    level = prompt("Level: ")
    correct = random.randrange(1, level + 1)
    while True:
        guess = prompt("Guess: ")

        if guess < correct:
            print("Too small!")
        elif guess > correct:
            print("Too large!")
        else:
            print("Just right!")
            break

main()
