
# to define a tuple use () or not

tup = 11,22,33,44
print(type(tup))

# OR

myTuple = (99,55,33,66)
print(type(myTuple))

print(min(myTuple)) # 33
print(max(myTuple)) # 99
print(sum(myTuple)) # 253

print(tup[1])

# can use tuple as object like employee...
employee = (1,'Ibrahim',38,'Developer')
Id,name,age,job =employee
print(Id) # 1
print(name) # Ibrahim
print(age) # 38
print(job) # Developer

# can store list in tuple like that...
tup2 = (1,'Ibrahim',[11,55,33])
print(tup2) # (1, 'Ibrahim', [11, 55, 33])

#can change the list inside tuple
tup2[2][2] = 99
#first number index of the element list ...
# scenod number the index want to change ...
print(tup2) # (1, 'Ibrahim', [11, 55, 99])

# to check the value in tuple use (in)
print(1 in tup2) # True

myTup = (44)
print(type(myTup)) #<class 'int'> that because it's one value

myTup2 = (44,)
print(type(myTup2)) # <class 'tuple'> not one value now

