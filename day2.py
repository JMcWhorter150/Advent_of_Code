def list_modification(list):
    for index in range(0, len(list), 4):
        if list[index] == 99:
            return list
        elif list[index] == 1:
            num1 = list[list[index+1]]
            num2 = list[list[index+2]]
            try:
                list[list[index+3]] = num1 + num2
            except IndexError:
                return list
        elif list[index] == 2:
            num1 = list[list[index+1]]
            num2 = list[list[index+2]]
            try:
                list[list[index+3]] = num1 * num2
            except IndexError:
                return list
    return list

# print(list_modification([1, 0, 0, 0, 99]))
# print(list_modification([2,3,0,3,99]))
# print(list_modification([2,4,4,5,99, 0]))
# print(list_modification([1,1,1,4,99,5,6,0,99]))

# list = [1,1,1,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,10,19,2,9,19,23,2,23,10,27,1,6,27,31,1,31,6,35,2,35,10,39,1,39,5,43,2,6,43,47,2,47,10,51,1,51,6,55,1,55,6,59,1,9,59,63,1,63,9,67,1,67,6,71,2,71,13,75,1,75,5,79,1,79,9,83,2,6,83,87,1,87,5,91,2,6,91,95,1,95,9,99,2,6,99,103,1,5,103,107,1,6,107,111,1,111,10,115,2,115,13,119,1,119,6,123,1,123,2,127,1,127,5,0,99,2,14,0,0]
# print(list_modification(list))

def determine_starting_number(noun, verb):
    list = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,10,19,2,9,19,23,2,23,10,27,1,6,27,31,1,31,6,35,2,35,10,39,1,39,5,43,2,6,43,47,2,47,10,51,1,51,6,55,1,55,6,59,1,9,59,63,1,63,9,67,1,67,6,71,2,71,13,75,1,75,5,79,1,79,9,83,2,6,83,87,1,87,5,91,2,6,91,95,1,95,9,99,2,6,99,103,1,5,103,107,1,6,107,111,1,111,10,115,2,115,13,119,1,119,6,123,1,123,2,127,1,127,5,0,99,2,14,0,0]
    list[1] = noun
    list[2] = verb
    new_list = list_modification(list)
    return new_list[0]


#only works for 0-99 for the noun and verb
def compare_starting_value(value_to_check):
    for i in range(99):
        for j in range(99):
            if value_to_check == determine_starting_number(i, j):
                return i, j

# print(compare_starting_value(19690720))

print(determine_starting_number(64, 72))
# print(determine_starting_number(list, 12, 2))
# def determine_noun_and_verb(lst):
#     for i in range(0, 99):
#         for j in range(0, 99):
#             working_list = lst
#             working_list[1] = i
#             working_list[2] = j
#             print(list_modification(working_list)[0])
#             # print(working_list[0])
#             if working_list[0] == 19690720:
#                 return working_list

# print(determine_noun_and_verb(list))