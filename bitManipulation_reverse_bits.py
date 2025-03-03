# Reverse Bits
# Tags: N190, Blind75, Bit manipulation, Easy

def reverseBits(self, n: int) -> int:
        
    res = 0
    for i in range(32):
        bit = (n >> i) & 1
        res = res | bit << (31-i)
            
    return res

n = 00000010100101000001111010011100
reverseBits(n)

# Time complexity : O(1)
# Space complexity : O(1)

# Input: n = 00000010100101000001111010011100
# Output:    964176192 (00111001011110000010100101000000)

