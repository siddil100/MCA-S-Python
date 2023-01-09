lrange=int(input("Enter the first ramge: "))
frange=int(input("Enter the second ramge: "))
first = 0
second = 1
print(first)
print(second)
for x in range(lrange,frange+1):
    third = first + second
    print(third)
    first,second=second,third