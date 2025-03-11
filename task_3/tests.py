import unittest

from task_3 import Student


class TestStudent(unittest.TestCase):
    def test_valid_student(self):
        student = Student("Оксана", "Захарченко", 20, 4.2)
        self.assertEqual(student.first_name, "Оксана")
        self.assertEqual(student.last_name, "Захарченко")
        self.assertEqual(student.age, 20)
        self.assertEqual(student.gpa, 4.2)

    def test_invalid_name(self):
        with self.assertRaises(ValueError):
            Student("Ольга123", "Петренко", 20, 4.5)

    def test_invalid_surname(self):
        with self.assertRaises(ValueError):
            Student("Ольга", "Петр3нко", 20, 4.5)

    def test_invalid_age(self):
        with self.assertRaises(ValueError):
            Student("Ольга", "Петренко", 15, 4.5)

    def test_invalid_gpa(self):
        with self.assertRaises(ValueError):
            Student("Ольга", "Петренко", 20, 5.5)

if __name__ == "__main__":
    unittest.main()
