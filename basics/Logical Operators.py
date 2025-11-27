
a= 4
b = 5

print(a< 10 and b > 1) # True
print(a< 10 and b > 12) # False
print(a > 10 and b > 1) # False
print(a > 10 and b > 13) # False

print(a< 10 or b > 1) # True
print(a< 10 or b < 1) # True
print(a< 2 or b > 1) # True
print(a< 2 or b > 15) # False

result = True
print(result) # True
print(not result) # False