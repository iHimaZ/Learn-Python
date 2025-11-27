# to define a set use {}

# set is collection of unordered unique elements
# every value in a set goes called (Hashing)

set1 = {23,56,78,21,56}
print(set1) # {56, 21, 78, 23}

print(21 in set1)
print(len(set1))
print(type(set1))

# if define the set like this set3 = {}
# that type of set is dict means (dictionary)
set3 = {}
print(set3)
print(type(set3)) # <class 'dict'>

# to define set as set type use set()
set4 = set()
print(type(set4)) # <class 'set'>

set6 = set('Ibrahim')
print(set6) # {'h', 'a', 'i', 'm', 'b', 'I', 'r'}

set5 = set('Mahmoud')
print(set5) # {'h', 'o', 'd', 'u', 'a', 'm', 'M'}

# take all char in set6 is not exists in set5
print(set6 - set5) # {'i', 'b', 'r', 'I'}

# takes all in two set5,6 without duplicate char
print(set6 | set5) # {'M', 'h', 'o', 'd', 'a', 'i', 'm', 'b', 'I', 'u', 'r'}

# takes only char are exists in two sets
print(set6 & set5) # {'a', 'h', 'm'}

# takes all different chars only from two sets
print(set6 ^ set5) # {'o', 'd', 'u', 'i', 'b', 'I', 'M', 'r'}



# carrot -> ^