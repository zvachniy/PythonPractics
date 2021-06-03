my_matrix = [
    [1, -2, -3, 4, 0],
    [0, 6, -7, -8, 0],
    [0, 11, 0, -13, 14],
    [0, 0, -17, 18, -19]
]
my_dictionary_j = {}


def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print("{:4d}".format(matrix[i][j]), end="")
        print()
    print("\n")


def delete_not_positive_column(matrix):
    counter_set_j = 0
    for rows in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[rows][j] <= 0:
                counter_set_j += 1
                my_dictionary_j[j] = counter_set_j
    delete_column_j(matrix, find_max_dict_value(my_dictionary_j))


def find_max_dict_value(dict):
    max = 0
    max_key = 0
    for key, val in dict.items():
        if max <= val:
            max = val
            max_key = key
    return max_key


def delete_column_j(matrix, deleting_column):  # удаляем столбец
    rows = len(matrix)
    for i in range(rows):
        deleted = matrix[i].pop(deleting_column)


print_matrix(my_matrix)
delete_not_positive_column(my_matrix)
print_matrix(my_matrix)


