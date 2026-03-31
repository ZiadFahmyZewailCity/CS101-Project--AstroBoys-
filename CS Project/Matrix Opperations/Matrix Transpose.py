#User Sets dimensions of Matrix (MxN
dimension_matrices = input("Enter dimension of matrices in this format (mxn): ").split("x")

m = int(dimension_matrices[0])
n = int(dimension_matrices[1])

array_a = []

#Allows user to enter Matrix(mxn)
for i in range(m):
    length = False
    while length == False:
        array_row_m = input(f"Enter row {i + 1} of matrix A (format(ele(1),...,ele(n)): ").split(",")
        int_array_row_m = [int(i) for i in array_row_m]
        if len(array_row_m) == n:
            array_a.append(int_array_row_m)
            length = True
        else:
            print(f" Your row is not {n} elements long re-enter")
l_A_T = []

# This would only work for square matrices
for i in range(len(array_a[0])):
    l_A_T_row = []
    for k in range(len(array_a)):
        l_A_T_row += [array_a[k][i]]
    l_A_T.append(l_A_T_row)




print(l_A_T)










