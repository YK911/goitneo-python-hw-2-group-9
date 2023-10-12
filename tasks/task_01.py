from datetime import datetime
from collections import defaultdict

birthday_dict = defaultdict(list)
weekdays = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]


def get_birthdays_per_week(users):
    current_date = datetime.today().date()

    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=current_date.year)

        if birthday_this_year < current_date:
            birthday_this_year = birthday.replace(year=current_date.year + 1)

        delta_days = (birthday_this_year - current_date).days

        if delta_days < 7:
            if birthday_this_year.weekday() >= 5:
                birthday_dict[weekdays[0]].append(name)
            else:
                birthday_dict[weekdays[birthday_this_year.weekday()]].append(name)

    for day, users_list in birthday_dict.items():
        print(f"{day}: {', '.join(users_list)}")


users = [
    {"name": "Bill Gates", "birthday": datetime(1955, 10, 12)},
    {"name": "Jan Koum", "birthday": datetime(1965, 10, 17)},
    {"name": "Jill Valentine", "birthday": datetime(1975, 10, 10)},
    {"name": "Kim Kardashian", "birthday": datetime(1985, 10, 5)},
    {"name": "Dua Lipa", "birthday": datetime(1985, 10, 14)},
    {"name": "John Dou", "birthday": datetime(1985, 10, 14)},
]

if __name__ == "__main__":
    res = get_birthdays_per_week(users)
    print("res: ", res)
