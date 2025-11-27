
a = 10 # global variable

def something():
    globals()['a'] = 20
    print(globals()['a'])
    a = 15
    print("inside: ", a)

something()
print("outside: ", a)