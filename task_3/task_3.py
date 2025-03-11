# Завдання 3

# Створити клас, у який дозволяє зберігати дані про студента:

# - ім'я;

# - прізвище;

# - вік;

# - середній бал.

# Створіть список з 10 студентів-інстансів даного класу та протестуйте валідність даних використовуючи пакет unittest.

class Student():
    def __init__(self,
                 first_name:str,
                 last_name:str,
                 age:int,
                 gpa:float
                 ):
        if not first_name.isalpha():
            raise ValueError("Ім'я повинно містити лише літери")
        if not last_name.isalpha():
            raise ValueError("Прізвище повинно містити лише літери")
        if not (16 <= age <= 100):
            raise ValueError("Вік має бути у межах 16-100 років")
        if not (0.0 <= gpa <= 5.0):
            raise ValueError("Середній бал має бути у межах 0.0-5.0")

        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gpa = gpa

students = [
    Student("Ольга", "Петренко", 20, 4.5),
    Student("Іван", "Шевченко", 22, 3.8),
    Student("Марія", "Коваленко", 19, 4.9),
    Student("Артем", "Мельник", 21, 2.5),
    Student("Анна", "Сидоренко", 23, 3.2),
    Student("Максим", "Федоренко", 18, 4.1),
    Student("Наталія", "Григоренко", 24, 4.0),
    Student("Дмитро", "Лисенко", 25, 3.7),
    Student("Владислав", "Ткаченко", 20, 2.9),
    Student("Юлія", "Кравченко", 22, 3.5)
]
