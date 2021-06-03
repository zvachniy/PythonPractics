matrix = [
    [1, -2, -3, 4],
    [5, 6, -7, 8],
    [9, 10, -11, 12],
    [13, 14, -15, 16]
]
my_dictionary_i = {}
my_dictionary_j = {}
my_tuples = 0


def printMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print("{:4d}".format(matrix[i][j]), end="")
        print()


printMatrix(matrix)

counter: int = 0

del_column = 0
k = 0


def delete_not_positive_column(matrix):
    counter_i: int = 0
    counter_j: int = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] <= 0:
                counter_j = j



    return print(counter_i, counter_j)




delete_not_positive_column(matrix)

# for row in matrix:
#     for x in row:
#         print("{:4d}".format(x), end="")
#     print()


