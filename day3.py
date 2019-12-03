# generate a grid with empty strings of any size
def create_matrix(width, height):
    # create empty matrix
    empty_matrix = []
    # create columns/width
    empty_row = []
    while len(empty_row) < width:
        empty_row += " "
    while len(empty_matrix) < height:
        empty_matrix.append(empty_row)
    return empty_matrix

def print_matrix(matrix):
    for row in matrix:
        print(row)

matrix = create_matrix(7, 7)
print_matrix(matrix)


# two problems
# 1. Determine where the two lines cross
# 2. Determine which crossing is closer to the origin

# Determine the size of the grid = Combination of all ups, downs, lefts, and rights

