#condition elif now 

marks=int(input("Enter Marks"))

if(marks>=90) and (marks>=100):
    print("GRADE A")

elif(marks>=80) and (marks>=89):
    print("GRADE B")

elif(marks>=70) and (marks>=79):
    print("GRADE C")

elif(marks>=60) and (marks>=69):
    print("GRADE D")

else:
    print("FAIL")