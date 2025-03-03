# Counting Bits - No of 1's in binary representation for each values
# Tags: N338, Blind75, Bit manipulation, Easy

def countBits(self, n: int) -> List[int]:
    res = []
    for num in range(n + 1):
        count_ones = 0
        n = num # Use a temporary variable as n
        while n > 0:
            # Use logical anding with number and minus one,so getting rid of ones at each iteration
            n = n & (n-1)
            count_ones += 1
        res.append(count_ones)

    return res

# Time complexity : O(n log n)
# Space complexity : O (n)

n = 5
print(countBits(n))
# Output: [0,1,1,2,1,2] 
# Explanation - no of one in binary bits for each the values 
#0 --> 0
#1 --> 1
#2 --> 10
#3 --> 11
#4 --> 100
#5 --> 101
