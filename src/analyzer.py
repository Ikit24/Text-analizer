class TextAnalyzer:
    def __init__(self):
        pass
    
    def count_words(self, text):
        if not text:
            return 0
        words = text.split()
        return len(words)
    
    def count_chars(self, text):
        return len(text)