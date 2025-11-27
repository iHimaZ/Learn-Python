
#def calculate_numbers(num1,num2 = 0): # default arguments
    #result = num1+num2
    #return result


# (*) called a variable length arguments...
# (*) means takes many of values in this parameter

def calculate_numbers(num1,*num2):
    sum_num = num1
    for n in num2:
        sum_num += n
    return sum_num


result = calculate_numbers(10,5,1,2,3)
print(result)

def person(name,age):
    print("name: ", name)
    print("age: ", age)

person('ibrahim',38)
person(age= 39,name = 'himaaa')

print('----------------------------------------------')

# ** means a dictionary (key-value pair)
def person(name,**key_args):
    print('name: ',name)
    for key,value in key_args.items():
        print(key," : ",value)

person('Ibarhim',age=39,loc="Egypt",tech="python")

#name:  Ibarhim
#age  :  39
#loc  :  Egypt
#tech  :  python