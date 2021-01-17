import pygame


def main():
    # initialise
    pygame.init()

    # set window settings
    logo = pygame.image.load("logo75x75.jpeg")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("Sudoku Solver")

    # -----SETUP-----
    # set screen surface
    SURFACE_SIZE = 675
    surface = pygame.display.set_mode((SURFACE_SIZE, SURFACE_SIZE))

    # set colours
    black = pygame.Color(0, 0, 0, 0)
    white = pygame.Color(255, 255, 255, 0)
    red = pygame.Color(255, 0, 0, 0)
    green = pygame.Color(40, 200, 40, 0)
    blue = pygame.Color(0, 0, 255, 0)
    grey = pygame.Color(120, 120, 120, 0)
    background = pygame.Color(220, 220, 220)

    # set fonts
    title_font = pygame.font.SysFont("calibri", 60)
    grid_font = pygame.font.SysFont("calibri", 50)
    grid_small_font = pygame.font.SysFont("calibri", 20)

    # set keys
    NUMBER_KEYS = [pygame.K_0, pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4,
                   pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9]

    # set select box co-ords
    select_box = [None, None] # row, column

    # set grid constants
    BOX_LENGTH = SURFACE_SIZE/9

    # LOAD SUDOKU

    sudoku = [[8, 0, 0, 9, 3, 0, 0, 0, 2],
              [0, 0, 9, 0, 0, 0, 0, 4, 0],
              [7, 0, 2, 1, 0, 0, 9, 6, 0],
              [2, 0, 0, 0, 0, 0, 0, 9, 0],
              [0, 6, 0, 0, 0, 0, 0, 7, 0],
              [0, 7, 0, 0, 0, 6, 0, 0, 5],
              [0, 2, 7, 0, 0, 8, 4, 0, 6],
              [0, 3, 0, 0, 0, 0, 5, 0, 0],
              [5, 0, 0, 0, 6, 2, 0, 0, 8]]

    curr_sudoku = [[8, 0, 0, 9, 3, 0, 0, 0, 2],
                   [0, 0, 9, 0, 0, 0, 0, 4, 0],
                   [7, 0, 2, 1, 0, 0, 9, 6, 0],
                   [2, 0, 0, 0, 0, 0, 0, 9, 0],
                   [0, 6, 0, 0, 0, 0, 0, 7, 0],
                   [0, 7, 0, 0, 0, 6, 0, 0, 5],
                   [0, 2, 7, 0, 0, 8, 4, 0, 6],
                   [0, 3, 0, 0, 0, 0, 5, 0, 0],
                   [5, 0, 0, 0, 6, 2, 0, 0, 8]]

    solved_sudoku = [[8, 4, 6, 9, 3, 7, 1, 5, 2],
                     [3, 1, 9, 6, 2, 5, 8, 4, 7],
                     [7, 5, 2, 1, 8, 4, 9, 6, 3],
                     [2, 8, 5, 7, 1, 3, 6, 9, 4],
                     [4, 6, 3, 8, 5, 9, 2, 7, 1],
                     [9, 7, 1, 2, 4, 6, 3, 8, 5],
                     [1, 2, 7, 5, 9, 8, 4, 3, 6],
                     [6, 3, 8, 4, 7, 1, 5, 2, 9],
                     [5, 9, 4, 3, 6, 2, 7, 1, 8]]

    draw(sudoku, curr_sudoku, solved_sudoku,       surface, select_box)

    # -----PLAY GAME-----
    # define control loop variable
    running = True

    # main loop
    while running:

        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # solve sudoku
                    solve = 1
                if event.key in NUMBER_KEYS and select_box != [None, None]:
                    enter_value(curr_sudoku, NUMBER_KEYS.index(event.key), select_box)
                    select_box = [None, None]
                if event.key == pygame.K_r:
                    curr_sudoku = reset_sudoku(curr_sudoku, sudoku)
                    select_box = [None, None]
                if event.key == pygame.K_d:
                    new_sudoku(curr_sudoku, sudoku)
                    select_box = [None, None]

            if event.type == pygame.MOUSEBUTTONDOWN:
                select_box = move_select(event.pos, select_box)

            if event.type == pygame.QUIT:
                running = False

        draw(sudoku, curr_sudoku, solved_sudoku,       surface, select_box)


    #-----SOLVE-----

def draw(sudoku, curr_sudoku, solved_sudoku,       surface, select_box):
    background = pygame.Color(220, 220, 220)  # # ---------- REMOVE

    surface.fill(background)
    draw_grid(surface)
    draw_grid_features(sudoku, curr_sudoku, solved_sudoku,       surface, select_box)

    pygame.display.update()


def draw_grid(surface):
    BOX_LENGTH = 675/9  # # ---------- REMOVE
    SURFACE_SIZE = 675  # # ---------- REMOVE
    black = pygame.Color(0, 0, 0, 0)  # # ---------- REMOVE

    line_width = 2
    for line in range(9):
        line_pos = BOX_LENGTH * line
        if line % 3 == 0:
            line_width = 4
        else:
            line_width = 2
        pygame.draw.line(surface, black, (line_pos, 0), (line_pos, SURFACE_SIZE), line_width)  # x line
        pygame.draw.line(surface, black, (0, line_pos), (SURFACE_SIZE, line_pos), line_width)  # y line

    # draw bounding edges
    line_pos = (BOX_LENGTH * 9) - (line_width-1)
    pygame.draw.line(surface, black, (line_pos, 0), (line_pos, SURFACE_SIZE), 2*line_width)  # x boundary line
    pygame.draw.line(surface, black, (0, line_pos), (SURFACE_SIZE, line_pos), 2*line_width)  # y boundary line


def draw_grid_features(sudoku, curr_sudoku, solved_sudoku,       surface, select_box):
    BOX_LENGTH = 675/9  # # ---------- REMOVE
    black = pygame.Color(0, 0, 0, 0)  # # ---------- REMOVE
    grey = pygame.Color(120, 120, 120, 0)  # # ---------- REMOVE
    red = pygame.Color(255, 0, 0, 0)  # # ---------- REMOVE
    green = pygame.Color(40, 200, 40, 0)  # # ---------- REMOVE
    blue = pygame.Color(0, 0, 255, 0)  # # ---------- REMOVE
    title_font = pygame.font.SysFont("calibri", 60)  # # ---------- REMOVE
    grid_font = pygame.font.SysFont("calibri", 50)  # # ---------- REMOVE

    # draw grid features
    for row in range(9):  # defined size 9
        for col in range(9):  # defined size 9
            # draw values
            if (sudoku[row][col] != 0):
                '''
                (text_width, text_height) = grid_font.size(str(sudoku[row][col]))
                surface.blit(grid_font.render(str(sudoku[row][col]), 1, black),
                             (BOX_LENGTH*col + (25), BOX_LENGTH*row + 16))
                '''
                draw_value(row, col, black,     surface, sudoku)
            elif (curr_sudoku[row][col] != 0):
                '''
                (text_width, text_height) = grid_font.size(str(curr_sudoku[row][col]))
                surface.blit(grid_font.render(str(curr_sudoku[row][col]), 1, grey),
                             (BOX_LENGTH*col + (25), BOX_LENGTH*row + 16))
                '''
                draw_value(row, col, grey,     surface, curr_sudoku)

            if (curr_sudoku[row][col] != solved_sudoku[row][col] and curr_sudoku[row][col] != 0):
                # draw incorrect box
                draw_box([row, col], red, surface)

            if (select_box != [None, None]):
                # draw select box
                draw_box(select_box, green, surface)


def draw_value(row, col, colour,        surface, sudoku):
    BOX_LENGTH = 675/9  # # ---------- REMOVE
    grid_font = pygame.font.SysFont("calibri", 50)  # # ---------- REMOVE

    (text_width, text_height) = grid_font.size(str(sudoku[row][col]))
    surface.blit(grid_font.render(str(sudoku[row][col]), 1, colour),
                 (BOX_LENGTH * (col) + (25), BOX_LENGTH * (row) + 16))


def draw_box(coords, border_colour,         surface):
    BOX_LENGTH = 675/9  # # ---------- REMOVE

    pygame.draw.rect(surface, border_colour, pygame.Rect(coords[1] * BOX_LENGTH, coords[0] * BOX_LENGTH, BOX_LENGTH, BOX_LENGTH), width=4)


def move_select(position, select_position):
    BOX_LENGTH = 675/9  # # ---------- REMOVE

    select_position[0] = int(position[1]//BOX_LENGTH)
    select_position[1] = int(position[0]//BOX_LENGTH)
    return select_position


def enter_value(curr_sudoku, key, position):
    curr_sudoku[position[0]][position[1]] = key
    return curr_sudoku


def reset_sudoku(curr_sudoku, sudoku):
    curr_sudoku = sudoku
    return curr_sudoku


def new_sudoku(curr_sudoku, sudoku):
    # TODO get new sudoku
    return curr_sudoku, sudoku


if __name__ == "__main__":
    #  call main loop
    main()
