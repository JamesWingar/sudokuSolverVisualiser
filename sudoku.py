# *************************************************************************** #
# Python class to store and solve a Sudoku, input as a string representation  #
# *************************************************************************** #
import sys
import copy


class Sudoku:
    """ This class to store and solve a Sudoku.
    Input parameter: String Sudoku with empty squares as 0 or . (Length === 81)
    Contains follow member methods:
        create_grid(s): Returns 9x9 list from input string
        create_string(): Return string from 9x9 solved sudoku
        print_solution_string(): Returns solution as a string
        check_valid_lines(list, int, int, int): Returns if value in row and
            column is valid
        check_valid_box(list, int, int , int): Returns if value in 3x3 box
            is valid
        soduku_solver(list, row, column): Recursively called function get
            soduku solution
        solve(): Starts and returns the resursive solution
        print_sudoku(): Prints stored sudoku
        print_solution(): Print solution as a grid format
    """

    def __init__(self, sudoku_string):
        self.string = "".join(sudoku_string.split())
        self.sudoku = self.create_grid(self.string)
        self.solution = []

    def create_grid(self, string):
        grid = []
        count = 0

        if len(string) != 81:  # ensure 9x9 size for sudoku
            print(len(string))
            sys.stderr.write("Error: String passed was incorrect length for Sudoku class. \
Use '0' or '.' to represent empty values, length must equal 81\n")
            return False

        for row in range(9):  # defined size 9
            grid.append([])
            for col in range(9):  # defined size 9
                if string[count] in ['0', '.']:
                    grid[row].append(0)
                else:
                    grid[row].append(int(string[count]))
                count += 1

        return grid

    def create_string(self, sudoku):
        string = ""

        for row in range(9):
            for col in range(9):
                string += str(sudoku[row][col])

        return string

    def create_solution_string(self):

        if len(self.solution) < 1:
            sys.stderr.write("Error: Must call solve() for the solution\n")
            return False

        return self.create_string(self.solution)

    def check_valid_lines(self, sudoku, value, row, column):

        for index in range(len(sudoku)):
            if sudoku[row][index] == value or sudoku[index][column] == value:
                return False

        return True

    def check_valid_box(self, sudoku, value, row, column):
        y_min = row//3 * 3
        x_min = column//3 * 3

        for y in range(y_min, y_min+2):
            for x in range(x_min, x_min+2):
                if sudoku[y][x] == value:
                    return False

        return True

    def sudoku_solver(self, sudoku, row, column):

        if row > len(sudoku) - 1:  # end condition
            return True

        # skip to next box if already filled
        if sudoku[row][column] != 0:
            if column < len(sudoku) - 1:
                if self.sudoku_solver(sudoku, row, column+1):
                    return True
            else:
                if self.sudoku_solver(sudoku, row+1, 0):
                    return True
            return False

        # check empty box for valid values
        for value in range(1, 10):
            if self.check_valid_lines(sudoku, value, row, column) and \
                    self.check_valid_box(sudoku, value, row, column):
                sudoku[row][column] = value
                if column < len(sudoku) - 1:
                    if self.sudoku_solver(sudoku, row, column+1):
                        return True
                else:
                    if self.sudoku_solver(sudoku, row+1, 0):
                        return True

        # remove previous answer from board
        sudoku[row][column] = 0
        return False

    def solve(self):
        self.solution = copy.deepcopy(self.sudoku)
        self.sudoku_solver(self.solution, 0, 0)
        return self.solution

    def print_sudoku(self):

        print("Soduku:")
        for row in range(9):
            print(self.sudoku[row])

    def print_solution(self):

        if len(self.solution) < 1:
            sys.stderr.write("Error: Must call solve() for the solution\n")
            return False

        print("Soduku solution:")
        for row in range(9):
            print(self.solution[row])
