
number:float = 2.5
print(type(number)) # float

number:int = 5
print(type(number)) # int

number = 6*9j # complex
print(type(number)) # complex
print(number) #54j
# if try and char else getting error !!!

a = 5.6
b=int(a)
print(a) #5.6
print(b) #5
s = float(b)
print(s) #5.0

k = 6
c=complex(b,k)
print(c) #5+6j

# range
r = range(10)
print(r) # range(0,10)

# can use range with set :
set(r) # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

# first number the start
# second number is to end of to numbers
# third number is step
set(range(1,11,2))
#{1, 3, 5, 7, 9}

# --------------------------------------
# True is 1
# False is 0
# --------------------------------------
bo = b < k
print(bo) # True
print(type(bo))

myList = [25,520,22,223,12] # can repeate values
print(type(myList))

mySet = {15,22,50,36} # no repeate values
print(type(mySet))
print(mySet)

myTuple = (51,20,30,50,20) # can repeate values
print(type(myTuple))
print(myTuple)

str="navin"
str='a'
print(type(str))
print(str)

range(0,10)
print(list(range(10)))

print(list(range(2,12,2)))

d={'navin':'samsung', 'rahul':'Iphone','Loreen':'Oneplus'}

print(d.keys()) # getting keys
print(d.values()) # getting values
print(d['Loreen'])
print(d.get('navin'))



