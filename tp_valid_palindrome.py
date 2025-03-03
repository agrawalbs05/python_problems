# Valid Palindrome - reads the same forward and backward
# Tags: N125, Blind75, array,two pointer method,Easy

def isPalindrome(self, s: str) -> bool:

    # Solution 1 : Two pointer method
    new_str = ''
    for i in s:
        if i.isalnum():
            new_str += i.lower()
        
    l = 0
    r = len(new_str) -1
    while l < r:
        if new_str[l] == new_str[r]:
            l += 1
            r -= 1
        else:
            return False
    return True

    # Solution 2: Naive solution(simple)
    """
    s1 = s.lower()
    filter_list = [i for i in s1 if i.isalnum()]
    filter_str = "".join(filter_list)
    reverse = filter_str[::-1]
    if filter_str == reverse:
        return True
    else:
        return False
    """


s = "A man, a plan, a canal: Panama"
isPalindrome(s)