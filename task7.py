matrix =[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

def print_diagon_of_matrix(inputMatrix):
    diagon_list=[]
    diagon_list=[inputMatrix[i][i] for i in range(len(inputMatrix))]
    return diagon_list

def find_min_matrix(diag_list):
    min_elem_diag=0
    diag_list=[]
    min_elem_diag=min(diag_list)
    return min_elem_diag

# print(print_diagon_of_matrix(matrix))
print(find_min_matrix(print_diagon_of_matrix))