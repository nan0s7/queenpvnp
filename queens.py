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

def empty_arr():
	arr = []
	row = []
	size = 8
	for i in range(size):
		for j in range(size):
			row.append(0)
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
		for j in range(len(arr)):
			if i == col:
				row.append(set_to)
			else:
				row.append(arr[j][i])
		new_arr.append(row)
		row = []
	return new_arr

def verify_row(arr):
	verified_array = empty_arr()
	q_loc = []
	for i in range(len(board_arr)):
		for j in range(len(board_arr)):
			# 1 = the queen on initial board atm
			if board_arr[j][i] == 1:
				verified_array[j] = set_row(board_arr[j], i+1)
				#verified_array = set_col(verified_array, j, i)
	return verified_array

def verify_col(arr):
	verified_array = empty_arr()
	q_loc = []
	for i in range(len(board_arr)):
		for j in range(len(board_arr)):
			if board_arr[j][i] == 1:
				#verified_array[i] = set_row(board_arr[i], i)
				verified_array = set_col(verified_array, i, i+1)
	return verified_array

def verify_diag(arr):
	verified_array = empty_arr()
	# find q_pos
	for i in range(len(arr)):
		for j in range(len(arr)):
			if arr[j][i] == 1:
				start_pos = [i, j]
				start_pos = [q_pos[0] - (qpos[0] - 1), q_pos[1] - (q_pos[0] - 1)]
	while start_pos[0] <= 8:
		arr[start_pos[1]][start_pos[0]] = "x"
		start_pos[0] += 1
		start_pos[1] += 1
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

print("Row check:")
for row in test:
	print(row)

print()

print("Column check:")
for row in test2:
	print(row)

print()
print("Collisions (row, col): " + validate(test) + ", " + validate(test2))
