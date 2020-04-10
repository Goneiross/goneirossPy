def printMatrix(A):
    """
    @param A: matrix
    """
    for row in A:
        for val in row:
            print (val, " ", end='')
        print()

def gauss(A, b):    
    """
    @param A: matrix
    @param b: vector
    @return: reduced echelon form of A|b
    """
    n = len(A)
    for i in range (0,n):
        if A[i][i] != 0:
            p = 1 / A[i][i]
            for j in range (i,n):
                A[i][j] *= p
            b[i]*p
            for k in range(i+1,n):
                for j in range(i+1,n):
                    A[k][j] -= A[k][i]*A[i][j]
                b[k] -= A[k][i]*b[i]
                A[k][i]=0 
    return A,b

def solveLower2Diag(A,b):
    """
    @param A: lower two diagonal matrix
    @param b: vector
    @return: b solutions
    """
    b[0] /= A[0][0]
    for i in range (1, n-1):
        b[i] =(b[i] - A[i][i-1]*b[i-1]) / A[i][i]
    return b

def choleskiTriDiag(A):
    """
    @param A: tridiagonal symetric positive definite matrix
    @return: L such taht A=LLT
    """
    L=[]
    n = len(A)
    for i in range(n):
        L.append([])
        for j in range(n):
            L[i].append(0)
    L[1][1] = sqrt(A[1][1])
    for i in range(1, n-1):
        L[i+1][i] = A[i+1][i]/L[i][i]
        l[i+1][i+1] = sqrt(A[i+1][i+1] - L[i+1][i])
    return L