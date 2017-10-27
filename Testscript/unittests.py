#coding=utf-8

import unittest

class  Test(unittest.TestCase):
    def setUp(self):
        number = input("enter a number")
        self.number= number

    def test_case(self):
        self.assertEqual(self.number,10,msg="you input is not 10")

    def tearDown(self):
        passs

if __name__ == '__main__':
 unittest.main()
