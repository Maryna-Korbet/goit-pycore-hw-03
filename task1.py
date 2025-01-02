from datetime import datetime

def get_days_from_today(date: str) -> int:

    try:
        target_date = datetime.strptime(date, '%Y-%m-%d').date()
        current_date = datetime.today().date()
        difference = (target_date - current_date).days
        return difference
    except ValueError as e:
        print(f"Date processing error: {e}")
        return 0
    

print (f"Difference in days: {get_days_from_today("2021-10-09")}");




