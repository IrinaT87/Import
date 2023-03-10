from datetime import date

from Application.salary import calculate_salary
from Application.db.people import get_employees

def get_date():
    date_is = date.today()
    print("Date_is:", date_is.strftime("%d.%m.%Y"))




if __name__ == '__main__':
    get_date()
    calculate_salary()
    get_employees()