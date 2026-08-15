months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]

while True:
    date = input("Date: ").strip()

    if "/" in date:
        parts = date.split("/")
        try:
            month, day, year = (int(p) for p in parts)
        except ValueError:
            continue
    else:
        parts = date.split(" ")
        try:
            month_name, day_str, year_str = parts
            day = int(day_str.rstrip(","))
            year = int(year_str)
        except (ValueError, IndexError):
            continue
        if month_name not in months:
            continue
        month = months.index(month_name) + 1

    if not (1 <= month <= 12 and 1 <= day <= 31):
        continue

    print(f"{year:04d}-{month:02d}-{day:02d}")
    break