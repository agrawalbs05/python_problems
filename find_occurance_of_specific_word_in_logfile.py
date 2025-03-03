def count_word_occurrences(filename, word):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            words = file.read().lower().split()  # Convert to lowercase for case-insensitive matching,split by whitespace
            return words.count(word.lower())  # Count occurrences of the word
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return 0

# Example usage
logfile = "logfile.txt"
word_to_find = "error"
occurrences = count_word_occurrences(logfile, word_to_find)
print(f"The word '{word_to_find}' appears {occurrences} times in {logfile}.")