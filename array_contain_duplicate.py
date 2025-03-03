# Check array contains duplicate
# Tags: N217, Blind75,array, Easy

def containsDuplicate(nums):
    # my_set = {} can not used as it creat empty dict not set. print(type(my_set)) 
    my_set = set()
    for i in nums:
        if i in my_set:
            return True
        else:
            my_set.add(i)

    return False

# Search,insert and remove operations has O(1) time coplexity.

nums = [1,2,3,1]
containsDuplicate(nums)
