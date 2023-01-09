x=int(input("Enter a number to check factor: "))
print('the factors are:')
for i in range(1, x + 1):
       if x % i == 0:
           print(i)