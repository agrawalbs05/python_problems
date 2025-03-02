# Binary search in sorted list
# Tags: N704, Blind75, Binary Search(O(log n)),array, Easy

def binary_search(nums, target):
    l = 0 
    r = len(nums) - 1
    while l <= r:
        mid = (l + r) // 2 
        if nums[mid] == target:
            return mid
            
        elif nums[mid] > target: #that means continue to search left 
            r = mid - 1
            
        else:
            l = mid + 1 #if nums at mid is less than target then continue to search right
    return -1
                  
nums = [-1,0,3,5,9,12]
target = 9
binary_search(nums,target)