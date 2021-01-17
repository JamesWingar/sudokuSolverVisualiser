# *************************************************************************** #
# Python class display a pygame gui to play and automate a game of Sudoku     #
# *************************************************************************** #
import pygame
import copy

# Set constants
SURFACE_SIZE = 675
BOX_LENGTH = SURFACE_SIZE/9
NUMBER_KEYS = [pygame.K_0, pygame.K_1,
               pygame.K_2, pygame.K_3,
               pygame.K_4, pygame.K_5,
               pygame.K_6, pygame.K_7,
               pygame.K_8, pygame.K_9]
EXIT_KEYS = [pygame.K_SPACE, pygame.K_ESCAPE,
             pygame.K_RETURN, pygame.K_BACKSPACE]


class Sudoku_solver:
    """ This class produces a pygame GUI for the backtracking
    Sudoku solver algorithm that you can play and automate (Brute forces)
    Input parameter: 
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

    def __init__(self, sudoku, solved_sudoku):
        # initialise
        pygame.init()

        # set window settings
        logo = pygame.image.load("logo75x75.jpeg")
        pygame.display.set_icon(logo)
        pygame.display.set_caption("Sudoku Solver")

        # set colours
        self.BACKGROUND = pygame.Color(220, 220, 220)
        self.BLACK = pygame.Color(0, 0, 0, 0)
        self.RED = pygame.Color(220, 20, 20, 0)
        self.GREEN = pygame.Color(50, 200, 50, 0)
        self.GREY = pygame.Color(120, 120, 120, 0)

        # set fonts
        self.title_font = pygame.font.SysFont("calibri", 60)
        self.grid_font = pygame.font.SysFont("calibri", 50)

        # set select box co-ords
        self.select_box = [None, None]

        # set screen surface
        self.surface = pygame.display.set_mode((SURFACE_SIZE, SURFACE_SIZE))

        # set multi-dimensional list sudoku's
        self.sudoku = sudoku
        self.current_sudoku = copy.deepcopy(sudoku)
        self.solved_sudoku = solved_sudoku

    def run(self):
        while(self.check_win()):
            for event in pygame.event.get():

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.select_box = [None, None]
                        self.current_sudoku = self.solve()
                    if event.key in NUMBER_KEYS and self.select_box != [None, None]:
                        self.enter_value(NUMBER_KEYS.index(event.key))
                        self.select_box = [None, None]
                    if event.key == pygame.K_r:
                        self.reset_sudoku()
                        self.select_box = [None, None]
                    if event.key == pygame.K_d:
                        self.new_sudoku()
                        self.select_box = [None, None]

                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.move_select(event.pos)

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            self.draw() 

        close = True
        while(close):
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key in EXIT_KEYS:
                        close = False

        return self.current_sudoku

    def solve(self):
        self.reset_sudoku()
        self.sudoku_solver(self.current_sudoku, 0, 0)
        return self.current_sudoku

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
            self.draw()
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

    def draw(self):
        self.surface.fill(self.BACKGROUND)
        self.draw_grid()
        self.draw_grid_features()

        pygame.display.update()

    def draw_grid(self):
        for line in range(9):
            line_pos = BOX_LENGTH * line
            if line % 3 == 0:
                line_width = 4
            else:
                line_width = 2
            pygame.draw.line(self.surface, self.BLACK, (line_pos, 0), (line_pos, SURFACE_SIZE), line_width)  # x line
            pygame.draw.line(self.surface, self.BLACK, (0, line_pos), (SURFACE_SIZE, line_pos), line_width)  # y line

        # draw bounding edges
        line_pos = (BOX_LENGTH * 9) - (line_width-1)
        pygame.draw.line(self.surface, self.BLACK, (line_pos, 0), (line_pos, SURFACE_SIZE), 2*line_width)  # x boundary line
        pygame.draw.line(self.surface, self.BLACK, (0, line_pos), (SURFACE_SIZE, line_pos), 2*line_width)  # y boundary line

    def draw_grid_features(self):
        for row in range(9):  # defined size 9
            for col in range(9):  # defined size 9
                # draw values
                if (self.sudoku[row][col] != 0):
                    # draw original sudoku value
                    self.draw_value(self.sudoku, row, col, self.BLACK)

                elif (self.current_sudoku[row][col] != 0):
                    # draw current sudoku value
                    self.draw_value(self.current_sudoku, row, col, self.GREY)

                if (self.current_sudoku[row][col] != self.solved_sudoku[row][col] and self.current_sudoku[row][col] != 0):
                    # draw incorrect box
                    self.draw_box([row, col], self.RED)

                if (self.select_box != [None, None]):
                    # draw select box
                    self.draw_box(self.select_box, self.GREEN)

    def draw_value(self, sudoku, row, col, value_colour):
        (text_width, text_height) = self.grid_font.size(str(sudoku[row][col]))
        self.surface.blit(self.grid_font.render(str(sudoku[row][col]), 1, value_colour),
                          (BOX_LENGTH*col + BOX_LENGTH/2 - text_width/2, BOX_LENGTH*row + BOX_LENGTH/2 - text_height/2))

    def draw_box(self, coords, border_colour):
        pygame.draw.rect(self.surface, border_colour, pygame.Rect(coords[1] * BOX_LENGTH, coords[0] * BOX_LENGTH, BOX_LENGTH, BOX_LENGTH), width=4)

    def move_select(self, position):
        self.select_box = [int(position[1]//BOX_LENGTH), int(position[0]//BOX_LENGTH)]

    def enter_value(self, key):
        if self.sudoku[self.select_box[0]][self.select_box[1]] == 0:
            self.current_sudoku[self.select_box[0]][self.select_box[1]] = key

    def reset_sudoku(self):
        self.current_sudoku = copy.deepcopy(self.sudoku)

    def new_sudoku(self):
        # TODO get new sudoku
        return self.current_sudoku, self.sudoku

    def check_win(self):
        return self.current_sudoku != self.solved_sudoku
