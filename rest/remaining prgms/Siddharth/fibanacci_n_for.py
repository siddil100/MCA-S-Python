frange=int(input("Enter a value for n: "))
first = 0
second = 1
print(first)
print(second)
for x in range(0,frange+1):
    third = first + second
    print(third)
    first,second=second,third