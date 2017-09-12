import random

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

def print_arr(arr):
	for i in arr:
		print(i)

def empty_arr():
	arr = []
	row = []
	size = 8
	for j in range(size):
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

def insert_in_arr(arr, pos, set_to):
	for i in range(len(arr[pos[1]])):
		
	return new_arr

def set_row(row, set_to):
	new_row = []
	for i in range(len(row)):
		new_row.append(set_to)
	return new_row

def set_col(arr, col, set_to):
	new_arr = []
	row = []
	for i in range(len(arr)):
		for j in range(len(arr)):
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
		for j in range(len(board_arr)):
			# 1 = the queen on initial board atm
			if board_arr[i][j] == 1:
				verified_array[i] = set_row(board_arr[i], j+1)
	return verified_array

def verify_col(arr):
	verified_array = empty_arr()
	q_loc = []
	for i in range(len(board_arr)):
		for j in range(len(board_arr)):
			if board_arr[i][j] == 1:
				verified_array = set_col(verified_array, j, i+1)
				break
	return verified_array

def verify_diag(arr):
	verified_array = empty_arr()
	start_pos = []
	# print_arr(verified_array)
	for i in range(len(arr)):
		for j in range(len(arr[i])):
			if arr[i][j] == 1:
				if (j == 0) and (i == 0):
					start_pos = [j, i]
				elif j > i:
					start_pos = [j - i, 0]
				elif i > j:
					start_pos = [0, i - j]
				else:
					print("Error calculating start_pos!")
				print(start_pos, end='')
				print(" col: " + str(j) + " row: " + str(i))
	while (start_pos[0] < 8) and (start_pos[1] < 8):
		# print(arr[start_pos[1]][start_pos[0]], end='')
		# print(start_pos)
		verified_array[start_pos[1]][start_pos[0]] = "x"
		start_pos[0] += 1
		start_pos[1] += 1
	# print_arr(verified_array)
	return verified_array

def validate(arr):
	result = "none"
	test_row = row_nums()
	test = []
	for i in range(len(arr)):
		for j in range(len(arr)):
			if arr[j][i] == 0:
				result = "collision"
			if not (arr[j][i] in test_row):
				test.append(arr[j][i])
			if len(test) > 0:
				result = "collision"
	return result

def pick_spot(arr):
	spot = random.randint(0, 8)

test = verify_row(board_arr)
test2 = verify_col(board_arr)
test3 = verify_diag(board_arr)

# print("Row check:")
# print_arr(test)
# print()
# print("Column check:")
# print_arr(test2)
print()
print_arr(test3)

print()
print("Collisions (row, col, dia): " + validate(test) + ", " + validate(test2) +\
		", " + validate(test3))
