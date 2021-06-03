matrix = [
    [1, -2, -3, 4],
    [5, 6, -7, 8],
    [9, 10, -11, 12],
    [13, 14, -15, 16]
]
my_dictionary_i = {}

my_tuples = 0


def printMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print("{:4d}".format(matrix[i][j]), end="")
        print()
    print("\n")


printMatrix(matrix)

counter: int = 0

del_column = 0
k = 0

my_dictionary_j = {}


def delete_not_positive_column(matrix):
    counter_set_j = 0
    rows = len(matrix)
    for j in range(rows):
        if matrix[j] <= 0:
            counter_set_j += 1
            my_dictionary_j[j] = counter_set_j
    delete_column_j(matrix, find_max_dict_value(my_dictionary_j))


def find_max_dict_value(dict):
    max = 0
    for val in dict.values():
        if max <= val:
            max = val
    return max


shadow_list = []


def delete_column_j(matrix, j):  # удаляем столбец
    rows = len(matrix)
    for i in range(rows):
        _ = matrix[i].pop(2)


delete_column_j(matrix)
printMatrix(matrix)
# delete_not_positive_column(matrix)
# printMatrix(shadow_list)
# for row in matrix:
#     for x in row:
#         print("{:4d}".format(x), end="")
#     print()
