# Group Anagrams
# Tags: N49 , Blind75, Array, Medium

def groupAnagrams(strs):
    # Use a dictionary where the key is the sorted version of the word, and the value is a list of anagrams   
    from collections import defaultdict
    anagram_map = defaultdict(list)
    for word in strs:
        sorted_word = "".join(sorted(word))  # Sort characters in the word
        anagram_map[sorted_word].append(word)  # Store in dictionary

    return list(anagram_map.values())  # Convert dict values to list
        
    """
    group = {}
    for i in strs:
        count = [0] * 26 #count array for each string
        for j in i:
            count[ord(j)-ord('a')] +=1 #increament count of each element
        key = tuple(count) #convert count array to a tuple for use as a dictionary key
        if key in group:
            group[key].append(i)
        else:
            group[key] = [i]
    return list(group.values()) 
    """     

strs = ["eat","tea","tan","ate","nat","bat"]
groupAnagrams(strs)