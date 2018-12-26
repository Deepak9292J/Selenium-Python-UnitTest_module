import unittest

class assertMethodDemo(unittest.TestCase):

    def test_assertTrueFalse(self):
        a = True
        self.assertTrue(a, "Test case failed, a is not true")
        b = False
        self.assertFalse(b, "Test case failed, b is not False")

    def test_assert_Equals(self):
        a = "Test"
        b = "Test"
        self.assertEqual(a , b, "a and b are not matching here")


if __name__ == '__main__':
    unittest.main(verbosity=2)
