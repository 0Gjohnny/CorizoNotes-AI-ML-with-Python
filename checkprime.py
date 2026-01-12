#check a number is prime or not 

count=0
num=int(input("enter a number"))
for i in range(1,num+1,1):
    if (num%i==0):
        count=count+1
if(count==2):
    print("Prime")
else:
    print("Non Prime")
        