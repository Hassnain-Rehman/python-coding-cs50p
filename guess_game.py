import random

while True:
    try:
        level = int(input("level: "))
        if level > 0:
            break
    except ValueError:
        pass

answer = random.randint(1, level)

while True:
    try:
        guess = int(input("guess: "))
        if guess <= 0:
            raise ValueError
    except ValueError:
        continue

    if guess < answer:
        print("Too small!")
    elif guess > answer:
        print("Too large!")
    else:
        print("Just right!")
        break
           #<<<<>>>>#
           