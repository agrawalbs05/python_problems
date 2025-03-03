# Count Occurrences of Each Element in a List
# Input: [1, 2, 2, 3, 4, 4, 4]; Output: {1: 1, 2: 2, 3: 1, 4: 3}

def count_occurrences(lst):
    from collections import Counter
    return dict(Counter(lst))

# Example usage
lst = [1, 2, 2, 3, 4, 4, 4]
occurrences = count_occurrences(lst)
print(occurrences)  # Output: {1: 1, 2: 2, 3: 1, 4: 3}
