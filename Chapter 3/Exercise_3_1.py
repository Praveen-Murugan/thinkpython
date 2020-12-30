"""
Exercise 3.5. This exercise can be done using only the statements and other features we have learned
so far.
Write a function that draws a grid like the following:
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +

Write a function that draws a similar grid with four rows and four columns.
"""



def do_four_with_two_arg(fn, valueone, valuetwo):
    fn(valueone, valuetwo)
    fn(valueone, valuetwo)
    fn(valueone, valuetwo)
    fn(valueone, valuetwo)
    
def generate_four_rows_for_columns(repfn, spacing, col_number):
    print_grid_head(spacing, col_number)
    repfn(print_grid_line, spacing, col_number)
    print_grid_head(spacing, col_number)
    repfn(print_grid_line, spacing, col_number)
    print_grid_head(spacing, col_number)
    repfn(print_grid_line, spacing, col_number)
    print_grid_head(spacing, col_number)
    repfn(print_grid_line, spacing, col_number)
    print_grid_head(spacing, col_number)


def print_grid_head(spacing, col_number):
    rep = " - " * spacing + "+"
    print("+", rep * col_number)


def print_grid_line(count, col_number):
    rep = "   " * count + "|"
    print("|", rep * col_number)


def generate_grid(spacing, col_number):
    print_grid_head(spacing, col_number)
    do_four_with_two_arg(print_grid_line, spacing, col_number)
    print_grid_head(spacing, col_number)
    do_four_with_two_arg(print_grid_line, spacing, col_number)
    print_grid_head(spacing, col_number)

generate_grid(4,2)
generate_four_rows_for_columns(do_four_with_two_arg, 4, 4)
