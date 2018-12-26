import unittest

class assertMethodDemo2(unittest.TestCase):

    def test_assertTrueFalse1(self):
        a = True
        self.assertFalse(a, "Test case failed, a is not true")
        b = False
        self.assertTrue(b, "Test case failed, b is not False")

    def test_assert_Equals1(self):
        a = "Test"
        b = "Test"
        self.assertEqual(a , b, "a and b are not matching here")


if __name__ == '__main__':
    unittest.main(verbosity=2)
