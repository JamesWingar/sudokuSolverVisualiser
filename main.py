import sudoku
import gui

'''
# easy - runtime (X with UI, X without UI)
puzzle = """800930002
009000040
702100960
200000090
060000070
070006005
027008406
030000500
500062008"""
'''

# medium - runtime (X with UI, X without UI)
puzzle = """000803001
480501000
000460050
060000009
078000310
500000040
050024000
000105074
800607000"""

'''
# hard - runtime (X with UI, X without UI)
puzzle = """091040000
200000600
080201003
000000708
008362500
405000000
500409070
007000004
000010830"""
'''

'''
# evil - runtime (X with UI, X without UI)
puzzle = """000007508
000090062
030400090
080000056
009000300
120000080
010006020
850070000
906800000"""
'''


def main():

    test = sudoku.Sudoku(puzzle)

    test.print_sudoku()

    test.solve()

    test.print_solution()

    solver = gui.Sudoku_solver(test.sudoku, test.solution)

    solver.run()


if __name__ == "__main__":
    main()
