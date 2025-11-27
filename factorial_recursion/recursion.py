import sys
from time import sleep
sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())

count = 1

def greet():
    global count
    print('hello' , count)
    count +=1
    sleep(0.02)
    greet()

greet()