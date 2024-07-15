def get_matrix():
    m = int(input("Enter number of rows: "))
    n = int(input("Enter number of columns: "))
    matrix = []
    for i in range(m):
        row = []
        for j in range(n):
            row.append(int(input(f"Enter element for a[{i+1}][{j+1}]: ")))
        matrix.append(row)
    return matrix

def triangular(matrix):
    for i in range(1, len(matrix)):
        for j in range(i):
            if matrix[i][j] != 0:
                return False
    return True

def diagonal(matrix):
    sum_diag = 0
    for i in range(len(matrix)):
        sum_diag += matrix[i][i]
    return sum_diag

def transpose(matrix):
    result = []
    for i in range(len(matrix[0])):
        row = []
        for j in range(len(matrix)):
            row.append(matrix[j][i])
        result.append(row)
    return result

def sum_matrix(a, b):
    result = []
    for i in range(len(a)):
        row = []
        for j in range(len(a[0])):
            row.append(a[i][j] + b[i][j])
        result.append(row)
    return result

def subtract(a, b):
    result = []
    for i in range(len(a)):
        row = []
        for j in range(len(a[0])):
            row.append(a[i][j] - b[i][j])
        result.append(row)
    return result

def multiply(a, b):
    result = []
    for i in range(len(a)):
        row = []
        for j in range(len(b[0])):
            row.append(0)
        result.append(row)

    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(a[0])):
                result[i][j] += a[i][k] * b[k][j]
    return result

def saddle(matrix):
    saddle_points = []
    rows = len(matrix)
    cols = len(matrix[0])
    for i in range(rows):
        row_min = matrix[i][0]
        min_cols = [0]
        for j in range(1, cols):
            if matrix[i][j] < row_min:
                row_min = matrix[i][j]
                min_cols = [j]
            elif matrix[i][j] == row_min:
                min_cols.append(j)
        for col in min_cols:
            is_saddle = True
            for k in range(rows):
                if matrix[k][col] > row_min:
                    is_saddle = False
                    break
            if is_saddle:
                saddle_points.append((i + 1, col + 1))
    return saddle_points

def magic_square(matrix):
    n = len(matrix)
    common_sum = sum(matrix[0])
    
    for row in matrix:
        if sum(row) != common_sum:
            return False

    for col in range(n):
        col_sum = 0
        for row in range(n):
            col_sum += matrix[row][col]
        if col_sum != common_sum:
            return False

    diag1_sum = 0
    diag2_sum = 0
    for i in range(n):
        diag1_sum += matrix[i][i]
        diag2_sum += matrix[i][n - i - 1]
    if diag1_sum != common_sum or diag2_sum != common_sum:
        return False

    return True

print("\tSelect any of the following operations: ")
print("1: Check for upper triangular")
print("2: Sum of diagonal")
print("3: Transpose")
print("4: Sum of 2 matrices")
print("5: Subtract 2 matrices")
print("6: Multiply 2 matrices")
print("7: Find saddle point")
print("8: Check for magic square")

cmd = int(input("Enter operation number: "))

matrix_a = get_matrix()
if cmd in {4, 5, 6}:
    matrix_b = get_matrix()

if cmd == 1:
    print(triangular(matrix_a))
elif cmd == 2:
    print(diagonal(matrix_a))
elif cmd == 3:
    print(transpose(matrix_a))
elif cmd == 4:
    print(sum_matrix(matrix_a, matrix_b))
elif cmd == 5:
    print(subtract(matrix_a, matrix_b))
elif cmd == 6:
    print(multiply(matrix_a, matrix_b))
elif cmd == 7:
    print(saddle(matrix_a))
elif cmd == 8:
    print(magic_square(matrix_a))
else:
    print("Invalid!")
