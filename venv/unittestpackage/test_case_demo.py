import unittest

class testCaseDemo(unittest.TestCase):

    #This setup method is at the test case level- means it will be executed before every test case
    def setUp(self):
        print("I will run once before every test case")

    #This teardown method is at the test case level- means it will be executed after every test case
    def tearDown(self):
        print("I will run once after every test case")

    def test_method1(self):
        print("Running method 1")

    def test_method2(self):
        print("Running method 2")

#Instead of creating object of class, this is another method of running the class
if __name__ == '__main__':
    unittest.main(verbosity=2)


