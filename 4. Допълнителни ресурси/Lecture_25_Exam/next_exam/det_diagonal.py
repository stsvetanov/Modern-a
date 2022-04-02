def get_diagonal(matrix):
    matrix_size = len(matrix)
    diagonal = []
    for row in range(matrix_size):
        for col in range(matrix_size):
            if row == col:
                diagonal.append(matrix[row][col])

    return diagonal


matrix_1 = [[23,12,54], [34,75,29], [12,36,58]]

print(get_diagonal(matrix_1))