import os
print("Current working directory:", os.getcwd())

class TextAnalyzer:
    def __init__(self, filepath):
        self.filepath = filepath
        self.file_contents = self._read_file()

    def _read_file(self):
        try:
            with open(self.filepath) as f:
                return f.read()
        except FileNotFoundError:
            print(f"Error: File {self.filepath} not found")
            return ""
    
    def count_words(self):
        if not self.file_contents:
            return 0
        words = self.file_contents.split()
        return len(words)
    
    def count_characters(self):
        print("Current number of characters are:")
        counts = {}
        for char in self.file_contents:
            char = char.lower()
            if char not in counts:
                counts[char] = 1
            else:
                counts[char] += 1
            
        return counts

if __name__ == '__main__':
    file_path = os.path.join("..", "data", "Sample.txt")
    analyzer = TextAnalyzer(file_path)
    print(analyzer.count_characters())
