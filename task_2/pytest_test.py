from pytest import approx
from task_2 import body_mass_index


def test_bmi_normal():
    assert body_mass_index(1.75, 70) == approx(22.86, 0.01)

def test_bmi_underweight():
    assert body_mass_index(1.80, 55) == approx(16.98, 0.01)

def test_bmi_overweight():
    assert body_mass_index(1.65, 80) == approx(29.38, 0.01)

def test_bmi_obesity():
    assert body_mass_index(1.50, 100) == approx(44.44, 0.01)

def test_bmi_zero_height():
    if body_mass_index(0,60):
        raise AssertionError

def test_bmi_negative_height():
    if body_mass_index(-1.75, 70):
        raise AssertionError

def test_bmi_negative_weight():
    if body_mass_index(1.75, -70):
        raise AssertionError

def test_bmi_text_input():
    if body_mass_index("1.75", 70):
        raise TypeError

def test_bmi_text_input_2():
    if body_mass_index(1.75, "70"):
        raise TypeError

def test_bmi_zero_weight():
    if body_mass_index(1.75, 0):
        raise ValueError


if __name__ == '__main__':
    for item in dict(globals()):
        if item.startswith("test"):
            try:
                func = globals()[item]
                func()
            except AssertionError:
                print(f'Error in test: {item}')
            except ValueError:
                print(f'ValueError in test: {item}')
            except TypeError:
                print(f'ValueError in test: {item}')
