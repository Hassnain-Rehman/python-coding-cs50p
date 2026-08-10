while True:
    fraction = input("fraction: ")
    try:
        x, y = fraction.split("/")
        x = int(x)
        y = int(y)
        if x < 0 or y <= 0 or x > y:
            continue
        pct = round(x / y * 100)
        if pct <= 1:
            print("E")
        elif pct >= 99:
            print("F")
        else:
            print(f"{pct}%")
        break
    except (ValueError, ZeroDivisionError):
        continue

                 #<<<<>>>>#

