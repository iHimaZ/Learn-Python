
# import math
# Or
#from math import sqrt,ceil
# Or
import math as m


# to read description on any function
# use help('math') on python.exe

def calculate_numbers(num1,num2 = 0):
    result = num1+num2
    return result

#response = calculate_numbers(int(input("enter number 1")),int(input("enter number 2")))
response = calculate_numbers(5)
print(response)


m.ceil(55.4) # 60
m.floor(55.4) # 55

num = 25
print(m.sqrt(num))
