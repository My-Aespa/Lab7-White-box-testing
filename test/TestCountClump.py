import unittest
from source.CountClump import CountClump  # Assuming the class is defined in a file named CountClump.py

class TestCountClump(unittest.TestCase):

    def setUp(self):
        """Set up test fixture"""
        # The CountClump class does not require instance initialization since the method is static.
        pass

    def test_TC1(self):
        """TC1: Test with an empty list"""
        result = CountClump.count_clumps([])
        self.assertEqual(result, 0)

    def test_TC2(self):
        """TC2: Test with None as input"""
        result = CountClump.count_clumps(None)
        self.assertEqual(result, 0)

    def test_TC3(self):
        """TC3: Test with a single element"""
        result = CountClump.count_clumps([1])
        self.assertEqual(result, 0)

    def test_TC4(self):
        """TC4: Test with two identical elements"""
        result = CountClump.count_clumps([1, 1])
        self.assertEqual(result, 1)

    def test_TC5(self):
        """TC5: Test with different elements"""
        result = CountClump.count_clumps([1, 2, 3])
        self.assertEqual(result, 0)

    def test_TC6(self):
        """TC6: Test with three identical elements"""
        result = CountClump.count_clumps([1, 1, 1])
        self.assertEqual(result, 1)

    def test_TC7(self):
        """TC7: Test with two identical elements and another element"""
        result = CountClump.count_clumps([1, 2, 2, 3])
        self.assertEqual(result, 1)

    def test_TC8(self):
        """TC8: Test with multiple clumps"""
        result = CountClump.count_clumps([1, 1, 2, 2, 3, 3])
        self.assertEqual(result, 3)

# Creating a test suite
def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestCountClump('test_TC1'))
    suite.addTest(TestCountClump('test_TC2'))
    suite.addTest(TestCountClump('test_TC3'))
    suite.addTest(TestCountClump('test_TC4'))
    suite.addTest(TestCountClump('test_TC5'))
    suite.addTest(TestCountClump('test_TC6'))
    suite.addTest(TestCountClump('test_TC7'))
    suite.addTest(TestCountClump('test_TC8'))
    return suite

# Running the test suite
if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
