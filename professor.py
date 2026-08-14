import random

def main():
    level = get_level()
    score = 0
    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        correct = x + y
        for _ in range(3):
            try:
                answer = int(input(f"{x} + {y} = "))
            except ValueError:
                print("EEE")
                continue
            if answer == correct:
                score += 1
                break
            else:
                print("EEE")
        else:
            print(f"{x} + {y} = {correct}")
    print(f"Score: {score}")

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in (1, 2, 3):
                return level
        except ValueError:
            pass

def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    else:
        return random.randint(10 ** (level - 1), 10 ** level - 1)

if __name__ == "__main__":
    main()

                #<<<<<>>>>>#

