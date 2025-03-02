# Search in Rotated Sorted Array
# N33, Blind75, Binary Search(O(log n)),array, Medium

def search_rotated_array(nums, target):
        # For O(log n) time complexity - better than O(n) - Binary search time solution 
        l = 0
        r = len(nums) - 1
    
        while l <= r:
            mid = (l + r) // 2
        
            if nums[mid] == target:
                return mid
        
        # Left sorted portion
            if nums[l] <= nums[mid]:
                if nums[l] <= target <= nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
        # Right sorted portion
            else:
                if nums[mid] <= target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
    
        return -1
        # Tags: N33, Blind75, Binary Search(O(log n)),array, Medium

        
        # Following time complexity O(n)
        """
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            else:
                return -1
        """

nums = [4,5,6,7,0,1,2]
target = 0
search_rotated_array(nums,target)