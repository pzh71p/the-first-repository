import unittest
from class_programmer_employee import ProgrammerEmployee

class PromgrammerEmployeeTestCase(unittest.TestCase):
    def setUp(self):
        self.myself_employee = ProgrammerEmployee('red_alert', '3y', 2_0000)

    def test_default_employee(self):
        self.myself_employee.give_raise()
        self.assertEqual(self.myself_employee.salary, 2_5000)

    def test_give(self):
        self.myself_employee.give_raise(1_0000)
        self.assertEqual(self.myself_employee.salary, 3_0000)


if __name__ == '__main__':
    unittest.main()
