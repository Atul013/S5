import re
from collections import Counter

def find_most_frequent_words(file_path, num_words=10):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read().lower()
        words = re.findall(r'\b\w+\b', text)
        word_counts = Counter(words)
        return word_counts.most_common(num_words)

file_path = 'your_file.txt'
most_frequent_words = find_most_frequent_words(file_path)
for word, count in most_frequent_words:
    print(f'{word}: {count}')
