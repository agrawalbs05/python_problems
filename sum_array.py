# Program to find sum of array

def sum_arr(arr):
  sum = 0
  for i in range(len(arr)):

        sum = sum + arr[i]

  return sum

x = [1,2,5,1,1]
print(sum_arr(x))



# OR 
"""
def sum_arr(arr):

    sum = 0
    for i in arr:
        sum = sum + i
    return sum

x = [1,2,5,1,1]
print(sum_arr(x))

"""

# OR
#print(sum(x))