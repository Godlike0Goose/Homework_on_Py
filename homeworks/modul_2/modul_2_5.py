def  get_matrix (m,n,value):
    matrix  = [value] * m
    for i in range(m):
        matrix[i]=[value] * n
    return matrix
a = int(input("введите число строк"))
b = int(input("введите число столбцов"))
c = int(input("какое число повторять?"))
print(get_matrix(a,b,c))