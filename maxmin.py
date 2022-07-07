
import sys


def maxMin(k, arr):
    # given [1, 2, 3, 4, 10, 20, 30, 40, 100, 200]
    # k = 4
    

    arr.sort()#[1,2,3,4,10,20,30,40,100,200]
    min_diff = sys.maxsize

    for i in range(len(arr)-k+1):
        #          min(xxx,       [4]       -   [1] = 3)
        min_diff = min(min_diff, arr[i+k-1] - arr[i])
    return min_diff


print(maxMin(4, [1, 2, 3, 4, 10, 20, 30, 40, 100, 200]))
