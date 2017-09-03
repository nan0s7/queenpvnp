# to put n-queens on a nxn sized chessboard

board_arr = [\
    [0, 0, 1, 0, 0, 0, 0, 0], \
    [0, 0, 0, 0, 0, 1, 0, 0], \
    [0, 0, 0, 0, 0, 0, 0, 1], \
    [1, 0, 0, 0, 0, 0, 0, 0], \
    [0, 0, 0, 1, 0, 0, 0, 0], \
    [0, 0, 0, 0, 0, 0, 1, 0], \
    [0, 0, 0, 0, 1, 0, 0, 0], \
    [0, 1, 0, 0, 0, 0, 0, 0] \
]

def empty_arr():
    arr = []
    row = []
    size = 8
    for i in range(size):
        row.append(0)
    for i in range(size):
        arr.append(row)
    return arr

def row_nums():
    size = 8
    row = []
    for i in range(size):
        row.append(i+1)
    return row

def set_row(row, set_to):
    new_row = []
    for i in range(len(row)):
        new_row.append(set_to)
    return new_row

def set_col(arr, col, set_to):
    new_arr = []
    row = []
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if j == col:
                row.append(set_to)
            else:
                row.append(arr[i][j])
        new_arr.append(row)
        row = []
    return new_arr

def verify_row(arr):
    verified_array = empty_arr()
    q_loc = []
    for i in range(len(board_arr)):
        for j in range(len(board_arr[i])):
            if board_arr[i][j] == 1:
                verified_array[i] = set_row(board_arr[i], i+1)
                #verified_array = set_col(verified_array, j, i)
    return verified_array

def verify_col(arr):
    verified_array = empty_arr()
    q_loc = []
    for i in range(len(board_arr)):
        for j in range(len(board_arr[i])):
            if board_arr[i][j] == 1:
                #verified_array[i] = set_row(board_arr[i], i)
                verified_array = set_col(verified_array, j, i+1)
    return verified_array

def validate(arr):
    result = "none"
    test_row = row_nums()
    test = []
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == 0:
                result = "collision"
            if not (arr[i][j] in test_row):
                test.append(arr[i][j])
    if len(test) > 0:
        result = "collision"
    return result

test = verify_row(board_arr)
test2 = verify_col(board_arr)

print("Row check:")
for row in test:
    print(row)

print()

print("Column check:")
for row in test2:
    print(row)

print()
print("Collisions (row, col): " + validate(test) + ", " + validate(test2))