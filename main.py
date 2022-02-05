from application.salary import calculate_salary
from application.db.people import get_employees
import datetime

print(__name__)

if __name__ == '__main__':
    print(f'Текущее точнейшее время {datetime.datetime.now()}')
    print()
    calculate_salary()
    print()
    get_employees()
