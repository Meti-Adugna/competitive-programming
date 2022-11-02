import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    j = n-1
    numbers = arr[j]
    
    for i in range(j, -1, -1):
        if numbers < arr[i-1] and i >= 1:
            arr[i] = arr[i-1]
            print(' '.join(str(x) for x in arr))
        else: 
            arr[i] = numbers
            print(' '.join(str(x) for x in arr))
            break 

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
