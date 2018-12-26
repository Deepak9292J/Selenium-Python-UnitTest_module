import unittest

#Import all the classes which we want to run. This is done as below-
from unittestpackage.test_case_demo import testCaseDemo
from unittestpackage.test_case_demo_2 import testCaseDemo2
from unittestpackage.assert_demo_1 import assertMethodDemo
from unittestpackage.assert_demo_2 import assertMethodDemo2

#Get All the tests from class files under consideration
test_case_1 = unittest.TestLoader().loadTestsFromTestCase(testCaseDemo)
test_case_2 = unittest.TestLoader().loadTestsFromTestCase(testCaseDemo2)
test_case_3 = unittest.TestLoader().loadTestsFromTestCase(assertMethodDemo)
test_case_4 = unittest.TestLoader().loadTestsFromTestCase(assertMethodDemo2)

#Create a test suite combining all the classes under consideration
smoke_tests = unittest.TestSuite([test_case_1,test_case_2,test_case_3,test_case_4])

#Trigger the Run.
unittest.TextTestRunner(verbosity=2).run(smoke_tests)