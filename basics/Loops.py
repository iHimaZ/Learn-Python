i = 1
while i <= 5:
    print("Iam in loop " + str(i))
    i +=1

# --------------------------------
print('----------------------------------')

data = [2,'Navin',4.5,34,3,'Python Is Good','Loreen','AI']

index = 0
length = len(data)

while index < length:
    print(data[index])
    index +=1

#----------------------------------
print('----------------------------------')

for value in data:
    print(value)

print('----------------------------------')

for value in range(10):
    if value % 3 == 0:
        continue

    print(value)

print('----------------------------------')

for value in range(10):
    if value == 5:
        break
    print(value)

print("Bye")




