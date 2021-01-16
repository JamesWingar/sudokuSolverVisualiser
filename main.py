
def print_sudoku(sudoku):
	print("Solution:")
	for row in range(len(sudoku)):
		print(sudoku[row])


def check_valid_lines(sudoku, value, row, column):
	for index in range(len(sudoku)):
		if sudoku[row][index] == value or sudoku[index][column] == value:
			return False

		y_min = row//3 * 3
		y_max = (row//3 * 3) + 2
		x_min = column//3 * 3
		x_max = (column//3 * 3) + 2

		for y in range(y_min, y_max):
			for x in range(x_min, x_max):
				if sudoku[y][x] == value:
					return False
	return True


def sudoku_solver(sudoku, row, column):

	# end condition
	if row > len(sudoku) - 1:
		return True

	# skip to next box if already filled
	if sudoku[row][column] != 0:
		if column < len(sudoku) - 1:
			if sudoku_solver(sudoku, row, column+1):
				return True
		else:
			if sudoku_solver(sudoku, row+1, 0):
				return True
		return False

	# check empty box for valid values
	for value in range(1,10):
		if check_valid_lines(sudoku, value, row, column):
			sudoku[row][column] = value
			#print_sudoku(sudoku)
			if column < len(sudoku) - 1:
				if sudoku_solver(sudoku, row, column+1):
					return True
			else:
				if sudoku_solver(sudoku, row+1, 0):
					return True

	# remove previous answer from board
	sudoku[row][column] = 0
	return False

def main():

	grid = [[8, 0, 0, 9, 3, 0, 0, 0, 2],
			[0, 0, 9, 0, 0, 0, 0, 4, 0],
			[7, 0, 2, 1, 0, 0, 9, 6, 0],
			[2, 0, 0, 0, 0, 0, 0, 9, 0],
			[0, 6, 0, 0, 0, 0, 0, 7, 0],
			[0, 7, 0, 0, 0, 6, 0, 0, 5],
			[0, 2, 7, 0, 0, 8, 4, 0, 6],
			[0, 3, 0, 0, 0, 0, 5, 0, 0],
			[5, 0, 0, 0, 6, 2, 0, 0, 8],]

	#[0, 0, 0, 0, 0, 0, 0, 0, 0],

	sudoku_solver(grid, 0, 0)

	print_sudoku(grid)

if __name__ == "__main__":
	main()




