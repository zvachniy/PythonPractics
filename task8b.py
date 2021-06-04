matrix = [
    [1, -2, -3, 0, -1],
    [0, 5, -6, 1, -1],
    [0, 8, 0, 0, 0],
    [0, 0, -12, 1, -1],
    [1, 0, -1, 0, 0],
    [1, 0, -1, 0, -1],
]
shadow_matrix = [[0] * len(matrix) for a in range(len(matrix[0]))]
final_matrix = []


def change_rows_col(inputMatrix, changedMatrix):
    for i in range(len(inputMatrix)):
        for j in range(len(inputMatrix[i])):
            changedMatrix[j][i] = inputMatrix[i][j]


def print_matrix(inputMatrix):
    for i in range(len(inputMatrix)):
        for j in range(len(inputMatrix[i])):
            print("{:4d}".format(inputMatrix[i][j]), end="")
        print()
    print("\n")


def delete_not_positive_string(inputMatrix):
    i, j = 0, 0
    for i in range(len(inputMatrix)):
        if i < len(inputMatrix):
            counter = 0
            for j in range(len(inputMatrix[i])):
                if inputMatrix[i][j] < 0 or inputMatrix[i][j] == 0:
                    counter += 1
                if counter == len(inputMatrix[i]):
                    inputMatrix.pop(i)
        else:
            final_matrix = [
                [0] * len(shadow_matrix) for a in range(len(shadow_matrix[0]))
            ]
            change_rows_col(shadow_matrix, final_matrix)
            print_matrix(final_matrix)


print_matrix(matrix)
change_rows_col(matrix, shadow_matrix)
delete_not_positive_string(shadow_matrix)

