# Recursion - Function calling itself
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(6))  # Output: 8

# Time Complexity: O(2ⁿ) (Exponential, slow for large n).
# Space Complexity: O(n) (Recursion depth)
