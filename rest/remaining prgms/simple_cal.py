#simple calculator program
def add(p,q):
    p+q
    return p+q
def sub(p,q):
    p-q
    return p-q
def mul(p,q):
    p*q
    return p*q
def div(p,q):
    p/q
    return p/q
print("select an operation")
print("1.add")
print("2.subtract")
print("3.multiply")
print("4.divide")
choice=input("enter your choice 1/2/3/4: ")
num1=float(input("Enter the first number"))
num2=float(input("Enter the second number"))
if choice=='1':
    print(num1,"+",num2,"=",add(num1,num2))
elif choice=='2':
    print(num1, "-", num2, "=", sub(num1, num2))
elif choice=='3':
    print(num1, "*", num2, "=", mul(num1, num2))
elif choice=='4':
    print(num1, "/", num2, "=", div(num1, num2))
else:
    print("Invalid choice")
