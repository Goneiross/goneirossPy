def printMatrix(A):
    for row in A:
        for val in row:
            print (val, " ", end='')
        print()

def Gauss(A, b):
    n = len(A)
    for i in range (0,n):
        printMatrix(A) 
        if A[i][i] != 0:
            p = 1 / A[i][i]
            for j in range (i,n):
                A[i][j] *= p
            b[i]*p
            for k in range(i+1,n):
                for j in range(i+1,n):
                    A[k][j] -= A[k][i]*A[i][j]
                b[k] -= A[k][i]*b[i]
                A[k][i]=0 #
            print(i)
    return A