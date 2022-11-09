import unittest

from translator import english_to_french
from translator import french_to_english

class testEnglishtoFrench(unittest.TestCase):

    def test1(self):

  
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertNotEqual(english_to_french('None'), '   ')


class testFrenchtoEnglish(unittest.TestCase):

    def test1(self):
        self.assertNotEqual(french_to_english('None'), '   ')  
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

if __name__ == "__main__":
    unittest.main()

