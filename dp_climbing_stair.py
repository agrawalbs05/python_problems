# Climbing Stairs
# Tags : N70, Blind75, dynamic programing, Easy

def climbStairs(self, n: int) -> int:

    # DP - bottomup approch
    # the value creates fibonaci series 
    one,two = 1, 1 #last values/steps will always 1
        
    for i in range(n-1):
        temp = one
        one = one + two
        two = temp
            
    return one

n = 3
climbStairs(n)
# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
#1. 1 step + 1 step + 1 step
#2. 1 step + 2 steps
#3. 2 steps + 1 step