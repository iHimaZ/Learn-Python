import sys

num = 10
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

nump1=int(input("enter number 1"))
result=nump1%2

if result==0 and result==2:
    print("Even")
    if nump1>5:
        print("Greate")

if(result==1):
    print("Odd")
elif result==3:
    print("Odd")
else:
    print("the Num :"+str(nump1)+" not equal any number (:")

print("bye")

i=1
while i<=5:
    print("Hey " + str(i))
    i=i+1
# to passing value from outside
#y=int(sys.argv[1])
#b=int(sys.argv[2])
#x=y+b
#print(x)

#result=eval(input("enter expression"))
#print(result)



