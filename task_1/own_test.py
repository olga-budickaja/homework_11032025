from pytest import approx
from task_1 import car_speed


def test_car_speed_1():
    assert car_speed(1,1) == 1.0

def test_car_speed_2():
    for i in range(1, 50):
        for j in range(1,50):
            if car_speed(i,j) != approx(i / j):
                raise AssertionError

def test_car_speed_zero_distance():
    assert car_speed(0, 10) == 0.0


def test_car_speed_large_numbers():
    assert car_speed(1000000, 2000) == 500.0


def test_car_speed_fractional_values():
    assert car_speed(0.3, 0.1) == approx(3.0)


def test_car_speed_negative_distance():
    assert car_speed(-100, 10) == -10.0


def test_car_speed_zero_time():
    for i in range(1, 50):
        for j in range(0):
            raise AssertionError

if __name__ == '__main__':
    for item in dict(globals()):
        if item.startswith("test"):
            try:
                func = globals()[item]
                func()
            except AssertionError:
                print(f'Error in test: {item}')
