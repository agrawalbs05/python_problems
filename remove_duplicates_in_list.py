# Remove All Occurrences of Duplicates
# Input: [1, 2, 2, 3, 4, 4, 5]; Output: [1, 3, 5]

def remove_all_duplicates(lst):
    from collections import Counter
    counts = Counter(lst)
    return [item for item , count in counts.items() if count == 1]

# Example usage
lst = [1, 2, 2, 3, 4, 4, 5]
result = remove_all_duplicates(lst)
print(result)  # Output: [1, 3, 5]