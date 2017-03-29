import unittest

from ranzhi import Ranzhi


class RanzhiTestRunner():
    def run_tests(self):
        suite = unittest.TestSuite()
        suite.addTest(Ranzhi('test_ranzhi'))
        runner = unittest.TextTestRunner()
        runner.run(suite)


if __name__ == "__main__":
    ranzhi_test_runner = RanzhiTestRunner()
    ranzhi_test_runner.run_tests()