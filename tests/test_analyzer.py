import unittest
from src.analyzer import TextAnalyzer

class TestTextAnalyzer(unittest.TestCase):
    def setUp(self):
        self.analyzer = TextAnalyzer()
    
    def test_word_count(self):
        text = "Hello world, how are you?"
        result = self.analyzer.count_words(text)
        self.assertEqual(result, 5)
    
    def test_empty_string(self):
        text = ""
        result = self.analyzer.count_words(text)
        self.assertEqual(result, 0)
    
    def test_character_count(self):
        text = "Hello!"
        result = self.analyzer.count_chars(text)
        self.assertEqual(result, 6)

if __name__ == '__main__':
    unittest.main()