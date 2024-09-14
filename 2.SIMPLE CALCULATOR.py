#creating simple CALCULATOR in Python
print("simple calculator to perform some tasks")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplicarion")
print("4.Division")
val=int(input())
if val==1:
    a=float(input("Enter First Value  :"))
    b=float(input("Enter second value  :"))
    sum=a+b
    print("Sum of the Two numbers is", sum)
elif val==2:
    a=float(input("Enter First Value : "))
    b=float(input("Enter Second Value : "))
    sub=a-b
    print("Subtract of Two numbers is ",sub)
elif val==3:
    a=float(input("Enter First Value : "))
    b=float(input("Enter Second Value : "))
    mul=a*b
    print("Mul of Two numbers is ",mul)
elif val==4:
    a=float(input("Enter First Value : "))
    b=float(input("Enter Second value : "))
    div=a/b
    print("Div of Two numbers is ",div)
else:
    print("Please Enter the number as mentioned above")
