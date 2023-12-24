from datetime import datetime

def calculate_age(date: int) -> int:
    now = datetime.now()

    return now.year - date.year - ((now.month, now.day) < (date.month, date.day))

print(calculate_age(datetime.strptime(input("Enter date: "), "%d-%m-%Y")))