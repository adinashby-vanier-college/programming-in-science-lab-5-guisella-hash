# Example for n = 5:
# *****
# *   *
# *   *
# *   *
# *****
def hollow_square(n):
    result = ""

    for i in range(n):
        for j in range(n):
            if(i == 0 or j == 0 or i == n - 1 or j == n - 1):
                result += "*"
            else:
                result += " "   
        result += "\n"             
    return result.rstrip()

# print(hollow_square(5))
# print(hollow_square(2))
# print(hollow_square(1))           
    # return ""

# 1
# 12
# 123
# 1234
def number_pattern(n):
    result = ""

    for i in range(n):
        for j in range(i + 1):
            result += str(j + 1)
        result += "\n"
    return result.rstrip()

# print(number_pattern(5))
# result = result + ""
# Remember that spaces after does not matter therefore we don't use k.
# Everytime we go back to he beginning of the loop values become 0 such as j=0
# return ""



# Example: For n = 5, sum = 1 + 2 + 3 + 4 + 5 = 15
def sum_of_natural_numbers(n):
    return ""

# Example for n = 4:
#    *
#   ***
#  *****
# *******
def centered_star_pyramid(n):
    return ""
