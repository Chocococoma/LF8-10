import unittest

class testExamples(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Fooo'.isupper())

if __name__ == '__main__':
    unittest.main()
