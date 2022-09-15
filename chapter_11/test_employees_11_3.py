from Employee_11_3 import Employee
import unittest


class TestEmployeeClass(unittest.TestCase):

    def setUp(self):
        """The employee instance"""
        self.employee_obj = Employee('jake', 'mike', 35000)
        self.custom_salary_raise = 15000

    def test_give_default_raise(self):
        """This should add 5000 to the employee salary, Lets test that..."""
        self.employee_obj.give_raise()
        self.assertEqual(self.employee_obj.salary, 40000)

    def test_give_custom_raise(self):
        """This should add 10000 to the employee salary, Lets test that..."""
        self.employee_obj.give_raise(self.custom_salary_raise)
        self.assertEqual(self.employee_obj.salary, 50000)
    pass


if __name__ == '__main__':
    unittest.main()

