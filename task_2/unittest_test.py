import unittest

from task_2 import body_mass_index

class TestBodyMassIndex(unittest.TestCase):
    def test_bmi_normal(self):
        self.assertAlmostEqual(body_mass_index(1.75, 70), 22.86, places=2)

    def test_bmi_underweight(self):
        self.assertAlmostEqual(body_mass_index(1.80, 55), 16.98, places=2)

    def test_bmi_overweight(self):
        self.assertAlmostEqual(body_mass_index(1.65, 80), 29.38, places=2)

    def test_bmi_obesity(self):
        self.assertAlmostEqual(body_mass_index(1.50, 100), 44.44, places=2)

    def test_bmi_zero_height(self):
        with self.assertRaises(ValueError):
            body_mass_index(0, 60)

    def test_bmi_negative_height(self):
        with self.assertRaises(ValueError):
            body_mass_index(-1.75, 70)

    def test_bmi_negative_weight(self):
        with self.assertRaises(ValueError):
            body_mass_index(1.75, -70)

    def test_bmi_text_input(self):
        with self.assertRaises(TypeError):
            body_mass_index("1.75", 70)

    def test_bmi_text_input_2(self):
        with self.assertRaises(TypeError):
            body_mass_index(1.75, "70")

    def test_bmi_zero_weight(self):
        with self.assertRaises(ValueError):
            body_mass_index(1.75, 0)

if __name__ == '__main__':
    unittest.main()
