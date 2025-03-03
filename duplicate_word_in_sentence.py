# Count Duplicate Words in a Sentence
# Input: "this is a test this is only a test"; 
# Output: { 'this': 2, 'is': 2, 'a': 2, 'test': 2 }

def count_duplicate_words(sentence):
    words = sentence.split()
    from collections import Counter
    counts = Counter(words)
    return {word: count for word, count in counts.items() if count > 1}

# Example usage
sentence = "this is a test this is only a test"
result = count_duplicate_words(sentence)
print(result)  # Output: {'this': 2, 'is': 2, 'a': 2, 'test': 2}