# Number of 1 Bits.Also known as the Hamming weight
# Tags: N191, Blind75 , Bit manipulation, Easy
"""
Example 1:
Input: n = 11
Output: 3
Explanation:
The input binary string 1011 has a total of three set bits.

Example 2:
Input: n = 128
Output: 1
Explanation:
The input binary string 10000000 has a total of one set bit.
"""

def no_of_one_bit():
        # We can use logical anding with number and minus one,so getting rid of ones at each iteration
        count = 0 
        while n > 0:
            n = n & (n-1)
            count += 1
        return count
    

n = 2147483645
print(no_of_one_bit(n)) # The input binary string 1111111111111111111111111111101 has a total of thirty set bits.