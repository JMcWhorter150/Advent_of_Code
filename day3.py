# # generate a grid with empty strings of any size
# def create_matrix(width, height):
#     # create empty matrix
#     empty_matrix = []
#     # create columns/width
#     empty_row = []
#     while len(empty_row) < width:
#         empty_row += " "
#     # create height
#     while len(empty_matrix) < height:
#         empty_matrix.append(empty_row)
#     return empty_matrix

# def print_matrix(matrix):
#     for row in matrix:
#         print(row)

# # figure out what size matrix to make
# def get_same_direction(lst, direction):
#     # Find all the strings that start with U
#     new_lst = []
#     for item in lst:
#         if item[0] == direction:
#             new_lst.append(item)
#     return new_lst

# def sum_direction_total(lst):
#     sum = 0
#     for item in lst:
#         sum += int(item[1:]) # Assumption is the first character of each string in the list is a letter and the rest are numbers, turns it into a number, and adds it
#     return sum

# def get_4_matrix_dimensions(lst):
#     matrix_directions = ["U", "L", "R", "D"]
#     direction_totals = []
#     for direction in matrix_directions:
#         direction_totals.append(sum_direction_total(get_same_direction(lst, direction))) #filters main list to only that direction, sums the total amount, adds it to new list
#     return direction_totals

# def convert_to_2_dimensions(direction_totals):
#     width = direction_totals[1] + direction_totals[2]
#     height = direction_totals[0] + direction_totals[3]
#     return width, height

# def get_matrix_width_height(lst):
#     return convert_to_2_dimensions(get_4_matrix_dimensions(lst))


# # find the origin location
# def get_matrix_origin(matrix):
#     x = int(len(matrix[0])) / 2
#     y = int(len(matrix)) / 2
#     return x, y

# def draw_horizontal_line(line_directions, current_origin):
#     pass




# def main():
#     line_directions = ["U7", "R6", "D4", "L4", "U6", "L7", "D8", "R4", "L7", "D10"]
#     # line_directions = ["U4", "R2", "D1", "L2"]
#     width, height = get_matrix_width_height(line_directions)
#     matrix = create_matrix(width, height)
#     print_matrix(matrix)

# main()

# two problems
# 1. Determine where the two lines cross
# 2. Determine which crossing is closer to the origin

# Determine the size of the grid = Combination of all ups, downs, lefts, and rights

### Welp, doesn't work after talking to Jonathan. Requires way, way, way too much computing power to solve

dictionary = {}
def main():
    direction_list = ["U7", "R6", "D4", "L4", "U6", "L7", "D8", "R4", "L7", "D10"]
    direction_list2 = ["D2", "D1", "D2", "U4",]
    x_dictionary = {}
    y_dictionary = {}
    x_coordinate = 0
    y_coordinate = 0
    for item in direction_list2:
        if item[0] == "U":
            if x_coordinate not in x_dictionary:
                x_dictionary[x_coordinate] = []
            for number in range(y_coordinate, int(item[1:]) + y_coordinate + 1):
                x_dictionary[x_coordinate].append(number)
            y_coordinate += int(item[1:])
        elif item[0] == "D":
            if x_coordinate not in x_dictionary:
                x_dictionary[x_coordinate] = []
            for number in range((int(item[1:]) * -1) + y_coordinate + 1, y_coordinate, -1):
                x_dictionary[x_coordinate].append(number)
            y_coordinate += (int(item[1:]) * -1)
    print(x_dictionary)
        # elif item[0] == "D":
        #     x_dictionary[x_coordinate] = range(-1 * (item[:1]), 0)
# create empty dictionaries, one for x, one for y
# for each direction, u = positive y, d = negative y, l = negative x, r = positive x

main()