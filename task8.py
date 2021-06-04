my_matrix = [
    [1, -2, -3, 0, -1],
    [0, 5, -6, 1, -1],
    [0, 8, 0, 0, -1],
    [0, 0, -12, 1, -1]
]
my_dictionary_j = {}


def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print("{:4d}".format(matrix[i][j]), end="")
        print()
    print("\n")


def set_j_index_dict(dictionary, matrix):
  for Rows in range(len(matrix)):
        for j in range(len(matrix[Rows])):
            dictionary[j] = 0  


def delete_not_positive_column(matrix):
    CounterJ = 0
    j = 0
    for Rows in range(len(matrix)):
        for j in range(len(matrix[Rows])):
            if matrix[Rows][j] < 0 or matrix[Rows][j] == 0:
                my_dictionary_j[j] += 1
    delete_column_j(matrix, find_max_dict_value(my_dictionary_j))


def find_max_dict_value(dict):
    max = 0
    max_key = 0
    for key, val in dict.items():
        if max <= val:
            max = val
            max_key = key
    return max_key


def delete_column_j(matrix, DeletingColumn):  # удаляем столбец
    Rows = len(matrix)
    for i in range(Rows):
        DeletedColumn = matrix[i].pop(DeletingColumn)

set_j_index_dict(my_dictionary_j,my_matrix)
print_matrix(my_matrix)
delete_not_positive_column(my_matrix)
print_matrix(my_matrix)

