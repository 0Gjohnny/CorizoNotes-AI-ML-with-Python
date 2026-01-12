#1 print factors of a number [10 - 1,2,5,10 ]
#2 check a number is prime or not :8 > not prime, 7 < prime
#using for, while loop to solve this

num=int(input("enter a number"))
for i in range(1,num+1,1):
    if (num%i==0):
        print(i)