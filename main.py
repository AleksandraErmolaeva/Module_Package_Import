from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import date
from DateTimePersian import DateTimePersian 

if __name__ == '__main__':
    calculate_salary()
    get_employees()
    print(date.today())
    print('Сегодня', DateTimePersian(TIME=False), 'по Персидскому календарю')

