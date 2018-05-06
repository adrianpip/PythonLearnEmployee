from employee import Employee
import unittest
from   unittest.mock import patch

class testEmployeeClass(unittest.TestCase):

    employees = []

    @classmethod
    def setUpClass(self):
        print('setUpClass')

    @classmethod
    def tearDownClass(self):
        print('tearDownClass')
        
    def setUp(self):
        print('setUp method for Employee')
        self.emp1 = Employee('fred','nerk', 50e3)
        self.emp2 = Employee('TomasZ','ROSE') # assigned minimum wage
        self.employees = [self.emp1,self.emp2 ]

    def tearDown(self):
        pass
##        tot=0.0
##        print('tearDown method for Employee')
##        for emp in self.employees:
##            tot=tot+emp.salary
####        tot=58000
##        print('payroll='+str(tot))
##        return tot
    
    def test_name(self):
        print('test_name')
        self.assertEqual(self.emp1.firstName, "Fred")
        self.assertEqual(self.emp1.lastName, "Nerk")
    
    def test_email(self):
        print('test_email')
        self.assertEqual(self.emp1.email, "fred.nerk@company.com")
    
##    def test_nameChange(self):
##        print('test_nameChange')
##        #self.assertEqual(self.emp2.change_name('Tom de Rose'),'Tom de Rose')
##        self.emp2.change_name('Tom de Rose')
##        self.assertEqual(self.emp2.email,"tom_de_Rose@company.com")
        
##
##    def test_raise(self):
##        print('test_raise')
##        self.assertEqual(self.emp1.apply_raise_201805(), 50500)
##        self.assertEqual(self.emp2.apply_raise_201711(), 37252.8)
##
##    def test_tell_email(self):
##        with patch('employee.requests.get') as mocked_get:
##            mocked_get.return_value.ok = True
##            mocked_get.return_value.text = 'Success'
##
##            response = self.emp1.tell_email()
##            mocked_get.assert_called_with('http://127.0.0.1/')
##            self.assertEqual(response, 'Success')
##
##            mocked_get.return_value.ok = False
##            mocked_get.return_value.text = '_bad response!' 
##
##            response = self.emp2.tell_email()
##            mocked_get.assert_called_with('https://google.com.au/')
##            self.assertEqual(response, '_bad response!')
##
##            

if __name__ == "__main__":
    unittest.main()
