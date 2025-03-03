# string , Amazn
# Convert a string such as aaabbccdaa to a3b2c2d1a2

def compress_string(s):
    if not s:
        return ""
    
    result = []
    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result.append(s[i - 1] + str(count))
            print(result) # ['a3']
            count = 1
    
    # Append the last character and its count
    result.append(s[-1] + str(count))

    return "".join(result)

# Example usage
s = "aaabbccdaa"
compressed = compress_string(s)
print(compressed)  # Output: a3b2c2d1a2