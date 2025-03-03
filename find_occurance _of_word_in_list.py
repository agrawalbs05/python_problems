"""
from collections import Counter

words = ["apple", "banana", "apple", "orange", "banana", "apple"]
word_counts = Counter(words)

print(word_counts)  # Output: {'apple': 3, 'banana': 2, 'orange': 1}
print(word_counts["apple"])  # Output: 3

"""

from collections import Counter

def word_frequencies(word_list):
    return dict(Counter(word_list))

# Example usage
words = ["apple", "banana", "apple", "orange", "banana", "apple"]
freq = word_frequencies(words)
print(freq)  # Output: {'apple': 3, 'banana': 2, 'orange': 1}