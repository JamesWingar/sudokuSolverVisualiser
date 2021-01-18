# SudokuSolver

Sudoku solver supports being run on any Python environment (Tested python 3.8+) with the only requirement being the pygame library if requiring the GUI. Software will solve any Sudoku through a backtracking algorithm (Brute force), the Sudoku class requires a string input as a representation of the Sudoku, empty spaces should be replaced by 0 or .

## Install
Prerequisites
* [git](https://git-scm.com/downloads)
* [python3](https://www.python.org/download/releases/3.0/)
* [pip](https://pypi.org/project/pip/)
* [pygame](https://www.pygame.org/)

To install follow the instructions below:
1. Open a command line tool (eg. Linux -> Terminal, Windows -> Powershell)
2. Install [git](https://git-scm.com/downloads)
3. Change directory to where you want the MagicMirror using the `cd` command
4. 
```python
git clone https://github.com/JamesWingar/sudokuSolver
```
5. Change directory to inside the directory `mirror_project`
6. 
```python
pip install -r requirements.txt
```
7. You are ready to go!

(*Note: you can use a virtual environment at step 6 to install the packages*)

## Usage
* Green box is the select box, Red box states the value is wrong
* Select a box and enter a number key to add value to the box
* Enter 0 to remove the value
* Press R to reset the Sudoku
* Press space to start the backtracking algorithm
* Press space, escape, enter or backspace to exit when complete

## Sudoku.py
Class to store and solve a Sudoku.
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

## GUI.py
Class to display a pygame GUI for the backtracking Sudoku solver algorithm that you can play and automate (Brute forces)
Input parameter: - Base Sudoku puzzle multi-dimensional list
                 - Solved sudoku multi-dimensional list
Contains follow member methods:
    run(): Main (while) loop to run the Draw, Input and Solve of the program 
    solve(): Starts and returns the resursive/backtracking solution
    sudoku_solver(list, int, int): Recursively called function get
        soduku solution
    check_valid_lines(list, int, int, int): Returns if value in row and
        column is valid
    check_valid_box(list, int, int , int): Returns if value in 3x3 box
        is valid
    draw(): Draws grid and grid features
    draw_grid(): Draws the horizontal and vertical grid lines
    draw_grid_features(): Draws the box values, select box and error box
    draw_value(list, int, int, tuple): Draws colour value in specified box
    draw_box(list, tuple): Draws colour box around specified box
    move_select(position): Moves selection box
    enter_value(key): Enters given key into current selected co-ords
    reset_sudoku(): Resets the current sudoku
    new_sudoku(): TODO - will generate another Sudoku
    check_win(): Checks if current sudoku equals the solution

## ToDo
* Add generating new Sudoku feature
* Add backspace to remove current values
* Add ability to reset after algorithm has finished
* Add victory screen