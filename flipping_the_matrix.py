def flippingMatrix(matrix):
    n=len(matrix)
    s=0
    for i in range(n//2):
        for j in range(n//2):
            s+=max(matrix[i][j], matrix[i][n-j-1], matrix[n-i-1][j], matrix[n-i-1][n-j-1])
    return s
  
  print(flippingMatrix([[1,2,4,25],[3,4,41,634],[31,13,54,66],[77,25,76,33]]))
  
  
