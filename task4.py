from datetime import datetime, timedelta

date_format = "%Y.%m.%d"

def get_upcoming_birthdays(users):
    result = []
    current_date = datetime.today().date()
    current_year = current_date.year

    for user in users:
        birthdate = datetime.strptime(user['birthday'], date_format).date()
        birthdate = birthdate.replace(year=current_year)

        if birthdate < current_date:
            birthdate = birthdate.replace(year=current_year + 1)

        days_difference = (birthdate - current_date).days
        if days_difference > 7:
            continue

        congratulation_date = birthdate
        if birthdate.weekday() == 5:  
            congratulation_date += timedelta(days=2)
        elif birthdate.weekday() == 6:  
            congratulation_date += timedelta(days=1)


        if congratulation_date.year > current_year:
            congratulation_date = congratulation_date.replace(year=current_year + 1)

        result.append({
            "name": user["name"],
            "congratulation_date": congratulation_date.strftime(date_format)
        })

    return result

users = [
    {"name": "Maryna Korbet", "birthday": "1986.01.05"},
    {"name": "John Doe", "birthday": "1985.01.04"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Olena Moss", "birthday": "1998.01.03"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("List of upcoming birthdays:")
print(upcoming_birthdays)