# Check two sum,exactly one solution
# Tags: N1, Blind75,hashing,array, Easy
# nums = [2,7,11,15], target = 9

def twoSum(nums, target):
        # Soultion1: hashmap which work on unsorted array too
        # hashmap is nothing but dictionary structure which store key-value pairs
        hashmap = {} #val:index
        print(type(hashmap))
        for index,value in enumerate(nums):
            diff = target - value
            if diff in hashmap:
                return [index,hashmap[diff]]
            hashmap[value] = index #Keep adding value and index to hashmap
        
        # Soultion2: brutforce approch
        """
         for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]       
        """
        # Soultion3: brutforce approchThis will  work if sorted array(Two pointer method):
        """ 
        p1 = 0 
        p2 = len(nums)-1
        
        while p1 < p2:
            sum = nums[p1] + nums[p2]
            
            if sum == target:
                return [p1,p2]
            
            elif sum < target:
                p1 += 1
                
            else: 
                p2 -= 1
                
        return [-1,-1]
        #Time complexity O(n)
        """ 

       
nums = [2,7,11,15]
target = 9
twoSum(nums,target)