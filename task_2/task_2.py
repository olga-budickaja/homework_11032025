# Завдання 2
# Взяти функцію розрахунку маси тіла з Python Starter українською/Домашнє_завдання 8/Завдання 5. Покрити її 10 тестами,
# щоб перевірити роботоздатність, використовуючи заздалегідь валідні дані та навпаки(введення текстових даних у поля,
# від'ємні значення тощо).
# За необхідності взяти її та доопрацювати до максимально стабільного варіанту.
# В процессі тестування використати:

# - оператор assert;
# - pytest;
# -unittest.


def body_mass_index(height: float, weight: float) -> float:
    """
    This function returns a body mass index with values: height and weight
    """
    if not isinstance(height, (int, float)) or not isinstance(weight, (int, float)):
        raise TypeError("Зріст і вага мають бути числами.")

    if height <= 0 or weight <= 0:
        raise ValueError("Зріст і вага мають бути додатними значеннями.")

    return weight / (height ** 2)
