from collections import Counter

def word_frequencies_in_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            words = file.read().split()  # Splitting by whitespace
            word_counts = Counter(words)
        return dict(word_counts)
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return {}

# Example usage
logfile = "logfile.txt"
freq = word_frequencies_in_file(logfile)
print(freq)  # Output: {'word1': count1, 'word2': count2, ...}


"""
from collections import Counter

def count_word_occurrences(logfile):
    word_count = Counter()
    
    with open(logfile, 'r', encoding='utf-8') as file:
        for line in file:
            words = line.strip().split()  # Split line into words
            word_count.update(words)  # Update word count

    return word_count

# Example Usage
logfile = "log.txt"  # Replace with your log file path
word_counts = count_word_occurrences(logfile)

# Print top 10 most common words
for word, count in word_counts.most_common(10):
    print(f"{word}: {count}")
"""