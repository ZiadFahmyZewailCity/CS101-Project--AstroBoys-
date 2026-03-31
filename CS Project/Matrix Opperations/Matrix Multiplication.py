dimension_matrices = input("Enter dimension of matrices in this format (mxn): ").split("x")

m = int(dimension_matrices[0])
n = int(dimension_matrices[1])

array_a = []
array_b = []

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


print(array_a)

for i in range(m):
    length = False
    while length == False:
        array_row_m = input(f"Enter row {i + 1} of matrix B (format(ele(1),...,ele(n)): ").split(",")
        int_array_row_m = [int(i) for i in array_row_m]
        if len(array_row_m) == n:
            array_b.append(int_array_row_m)
            length = True
        else:
            print(f" Your row is not {n} elements long re-enter")

print(array_b)


array_c = []

