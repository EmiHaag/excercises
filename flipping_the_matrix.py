"""
This is a test excercise of the hackerrank web page. 

Given a 2n x2n matrix, a matrix for len == even number, you have to resolve: 
return the sum of the max value from each quadrant wich is able to flip with it's mirror value.
Mirrors numbers always 4, no matter how big is the matrix.

i.e.
[[1,2,4,25],[3,4,41,634],[31,13,54,66],[77,25,76,33]])
[ 1,  2,  4,   25]
[ 3,  4, 41,634]
[31,13,54,  66]
[77,25,76,  33]

the values: 
1, 25, 77, 33 are the first area
2,4,25,76 are the second one
3,634, 31, 66 are the third one
4, 41, 13, 54 are the last area

the sum of each maximum area are the values that you have to return.

In this example function returns : 841
"""

def flippingMatrix(matrix):
    n=len(matrix)
    s=0
    for i in range(n//2):
        for j in range(n//2):
            s+=max(matrix[i][j], matrix[i][n-j-1], matrix[n-i-1][j], matrix[n-i-1][n-j-1])
    return s
  
  print(flippingMatrix([[1,2,4,25],[3,4,41,634],[31,13,54,66],[77,25,76,33]]))
  
  
