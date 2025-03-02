# Find Minimum in Rotated Sorted Array
# N153, Blind75, Binary Search(O(log n)),array,Medium

def find_min(nums):
    l, r = 0, len(nums) - 1
    
    while l < r:
        mid = (l + r) // 2
        # mid is greater than right then minimum value in right side
        if nums[mid] > nums[r]:  
            l = mid + 1  # Min is in right half
        else:
            r = mid  # Min is in left half or is mid itself
    
    return nums[l]  # Min element

# Test cases
print(find_min([4,5,6,7,0,1,2]))  # Output: 0
print(find_min([3,4,5,1,2]))  # Output: 1
print(find_min([2,1]))  # Output: 1