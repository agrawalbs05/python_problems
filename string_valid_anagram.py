# Check valid anagram - no of char is same by re-arraging word
# Tags: N242, Blind75,string, Easy
#Input: s = "anagram", t = "nagaram"

from collections import Counter

def valid_anagram(s,t):
    return Counter(s)==Counter(t)


# Using sorting: Time complexity is O(nlogn) due to sorting
"""
def are_anagrams(s1, s2):
    # If lengths differ, they can't be anagrams.
    if len(s1) != len(s2):
        return False
    
    # Sort both strings and compare them.
    return sorted(s1) == sorted(s2)

# Example usage
s1 = "listen"
s2 = "silent"
result = are_anagrams(s1, s2)
print(result)  # Output: True
"""