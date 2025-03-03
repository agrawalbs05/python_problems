# Find Duplicate Pairs in a List of Tuples 
# Input: [(1, 2), (3, 4), (1, 2), (5, 6)]; Output: [(1, 2)]

def find_duplicate_tuples(lst):
    from collections import Counter
    counts = Counter(lst)
    return [item for item, count in counts.items() if count > 1]

# Example usage
lst = [(1, 2), (3, 4), (1, 2), (5, 6)]
result = find_duplicate_tuples(lst)
print(result)  # Output: [(1, 2)]