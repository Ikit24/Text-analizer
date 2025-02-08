def sort_on(dict):
    return dict["num"]

def main():
    path = 'G:\\Text-analizer\\data\\Sample.txt'
    print("\n----- Starting analysis -----")
    with open(path) as f:
        words = [word for line in f
                 for word in line.strip().split()]
        
    print(f"\nTotal number of words: {len(words)}")

    lowered_words = [words.lower() if isinstance(words, str) else words for words in words]
    lowered_words = set(lowered_words)

    print(f"\nTotal number of individual words: {len(lowered_words)}")

    letter_count = {}
    special_chars_count = {}
    special_chars = set('[@_!#$%^&*()<>?/\\|}{~:]')

    for word in words:
        for char in word:
            if char.isalpha():
                char = char.lower()
                if char not in letter_count:
                    letter_count[char] = 1
                else:
                    letter_count[char] += 1
            elif char in special_chars:
                if char not in special_chars_count:
                    special_chars_count[char] = 1
                else:
                    special_chars_count[char] += 1

    letter_list = []
    for letter, count in letter_count.items():
        letter_list.append({"char": letter, "num": count})
    letter_list.sort(reverse=True, key=sort_on)

    print("\n----- Individual Letters Count -----")
    for item in letter_list:
        print(f"The letter '{item['char']}' appears {item['num']} times")

    special_char_list = []
    for char, count in special_chars_count.items():
        special_char_list.append({"char": char, "num": count})
    special_char_list.sort(reverse=True, key=sort_on)

    print("\n----- Special Characters Count -----")
    for item in special_char_list:
        print(f"The special character '{item['char']}' appears {item['num']} times")

    print("\n--- End report ---")        

if __name__ == '__main__':
    main()