import string

# to define a list use []

nums = [45,87,21,24,99,101,105]
# or nums = [45,87,21,24,99]

# get first element
print(nums[0])

# get last element in list
print(nums[-1])

# to get two elements from list
print(nums[2:4])
#print [21,24]

# to get from specific index to end of list
print(nums[2:])
#print [21,24,99,101,105]

names:string = ['navin','harsh','kiran']
print(names)

#complex of list different data types
myComplex = ['navin',1.5,99,True]
print(myComplex)

# can combined two list in one
myList = [names,nums]
print(myList)
# will combined two list in one list
# [['navin', 'harsh', 'kiran'], [45, 87, 21, 24, 99, 101, 105]]
print(len(myList)) # will print 2
#['navin', 'harsh', 'kiran'] 0
#[45, 87, 21, 24, 99, 101, 105] 1

#to get element from lists of lists
print(myList[0][1])

myList2 = names + nums
print(myList2)
# ['navin', 'harsh', 'kiran', 45, 87, 21, 24, 99, 101, 105]

# append function
nums.append(33)
print(nums)

# count get 1 if the number in list and 0 if not
print(nums.count(99))

# index get the index of the value in list...
print(nums.index(99))

# will insert the value 90 in index 2 and all this value will be pushed
nums.insert(2,90)
print(nums)

# remove
nums.remove(21) # the value in lits to remove

print(nums.pop(3))  # to get value of index.. and will remove
print(nums) # [45, 87, 90, 99, 101, 105, 33]

# can use pop without index but it will remove last index from the list
print(nums.pop()) # will remove 33

del nums[2:3]
print(nums)

# to insert multi-values use extend
nums.extend([11,22,55,66])
print(nums)

# change the values
nums[2:4] = [80,90]
print(nums)

# reverse
nums.reverse()
print(nums)

#https://www.youtube.com/watch?v=DeriNSJ7Ev0&list=PLsyeobzWxl7omDoEYrrf3oXvXxa6MPgek&index=8