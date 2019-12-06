125730-579381
total_numbers = 0
def isAscending(num_str):
        for index in range(5, 0, -1):
            if num_str[index] >= num_str[index - 1]:
                continue
            else:
                return False
        return True

def hasDoubleLetters(num_str):
    double_letters = ["11", "22", "33", "44", "55", "66", "77", "88", "99", "00"]
    for item in double_letters:
        if item in num_str:
            item += item[0]
            if item not in num_str:
                return True
    return False

for number in range(125730, 579381):
    num_str = str(number)
    if hasDoubleLetters(num_str) and isAscending(num_str):
        total_numbers += 1


print(total_numbers)
