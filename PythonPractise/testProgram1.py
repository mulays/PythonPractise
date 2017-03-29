import unittest
#import mock
import Program1

class PrgramTestClass(unittest.TestCase):
    def setUp(self):
        self.param = 3

    def tearDown(self):
        pass

    def test1(self):
        a = Program1.A(self.param)
        print a
        self.assertEquals(a,True)

    def test1Negative(self):
        a = Program1.A(0)
        print a
        self.assertFalse(a)


if __name__ == '__main__':
    unittest.main()


'''
X less than 5
True
.X less than 5
True
F

Ran 2 tests in 0.009s

FAILED (failures=1)
Exit code:  True
'''

