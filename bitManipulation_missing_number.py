# Missing number
# Tags: N268, Blind75, Bit manipulation, Easy

# nums = [3,0,1]
# nums = [0,1]
# nums = [9,6,4,2,3,5,7,0,1]

"""
Given an array nums containing n distinct numbers in the range [0, n], 
return the only number in the range that is missing from the array.
"""

""" 
        nums.sort()
        n = len(nums) + 1
        for i in range(n):
            if i not in nums:
                return i
   
"""
def find_missing_number(nums):
    # Initialize result with 0
    missing = 0
    
    # XOR all numbers from 0 to n
    for i in range(len(nums) + 1):
        missing ^= i
    
    # XOR all elements in the array
    for num in nums:
        missing ^= num
    
    return missing

# Example usage:
nums = [3, 0, 1]
print(find_missing_number(nums))  # Output: 2