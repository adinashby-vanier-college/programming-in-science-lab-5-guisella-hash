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

print(hollow_square(5))
print(hollow_square(2))
print(hollow_square(1))           
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

print(number_pattern(4))
print(number_pattern(1))
print(number_pattern(3))
# result = result + ""
# Remember that spaces after does not matter therefore we don't use k.
# Everytime we go back to he beginning of the loop values become 0 such as j=0
# return ""



# Example: For n = 5, sum = 1 + 2 + 3 + 4 + 5 = 15
def sum_of_natural_numbers(n):
    result = 0 

    for i in range(1, n + 1):
        result += i
# result = result + i
# when insside i loop result wil =l keel chnaging according to previous result:
# i=[1,2,3,4,5] (if n=5)
# 1st iteration, where i=1, 0+1=1
# 2nd, where i becomes 2, 1+2=3
# 3rd, where i=3, result= result(3) + i(3) = 3+3=6
# 4th, where i=4, result= result(6) + i(4) = 10
# 5th, where i=5, result= result(10) + i(5) = 15
# 
    return result
print(sum_of_natural_numbers(5))
print(sum_of_natural_numbers(1))
print(sum_of_natural_numbers(0))
print(sum_of_natural_numbers(10))
print(sum_of_natural_numbers(3))

    # return ""
 

# Example for n = 4:
#    *
#   ***
#  *****
# *******
def centered_star_pyramid(n):
    result = ""

    for i in range(n):
        for j in range(n - i - 1):
            result += " "
# must not use j below for range because j is part of i loop and it resets to zero everytime we restart the i loop. Both j,k...
        for k in range(i * 2 + 1):
            result += "*"
        result += "\n"

    return result.rstrip()

print(centered_star_pyramid(4))
print(centered_star_pyramid(1))
print(centered_star_pyramid(3))

    # return ""
