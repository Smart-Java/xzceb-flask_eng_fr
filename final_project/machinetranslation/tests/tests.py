import unittest
import translator
from translator import french_to_english, english_to_french

class ModuleTest(unittest.TestCase):
    def test_french_to_english_modules(self):
        return self.assertEqual(french_to_english('Bonjour'), 'Hello')
    
    def test_english_to_french_modules(self):
        return self.assertEqual(english_to_french('Hello'), 'Bonjour')

    def test_null_input_for_french_to_english_modules(self):
        return self.assertIsNotNone(french_to_english(None))
    
    def test_null_input_for_english_to_french_modules(self):
        self.assertIsNotNone(english_to_french(None))
