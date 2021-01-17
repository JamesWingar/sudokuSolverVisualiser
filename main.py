import sudoku


def main():

    sudo = """800930002
    009000040
    702100960
    200000090
    060000070
    070006005
    027008406
    030000500
    500062008"""

    test = sudoku.Sudoku(sudo)

    test.print_sudoku()

    test.solve()

    test.print_solution()


if __name__ == "__main__":
    main()
