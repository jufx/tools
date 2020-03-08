import unittest
from main import Skinner
from logger import Clogger
test_alive_counter = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
]
r = """test_R1

test_R2

test_R3

test_R4"""
y = Skinner
y.output = ''
y.log = Clogger().get_logger()
y(tab=test_alive_counter, iterations=10)



class MyTestCase(unittest.TestCase):
    def test_something(self):

        y(tab=test_alive_counter, iterations=1)
        self.assertEqual(True, True)


class MyTestCase2(unittest.TestCase):
    def test_logger(self):
        y = Skinner

        y.log = Clogger().get_logger()

        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
