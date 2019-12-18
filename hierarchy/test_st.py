import unittest
from people import *

class Stud_test(unittest.TestCase):
    
    def test_avg(self):
        std = Student('Петров','Андрей','Олегович',datetime.date(2001,4,23), { 'История' : 5 , 'Иинформатика' : 3 , 'Философия' : 3 })
        self.assertEqual(std.avg(), 3.5)

    def test_create(self):
       st = Student(None, None, None, None, None)
       st2 = st.create()
       self.assertIsNot(st, st2)

if __name__ == '__main__':
    unittest.main()