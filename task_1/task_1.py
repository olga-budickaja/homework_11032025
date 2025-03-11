# Завдання 1

# Створити функцію, яка допоможе порахувати швидкість автомобіля. Набір даних, який використовується для розрахунку:

# * довжина шляху;

# * тривалість шляху.

# Створити 5-7 тестів використовуючи оператор assert.


def car_speed(distance:int,travel_time:int):
    if travel_time !=0:
        return distance / travel_time
    else:
        raise ValueError()
