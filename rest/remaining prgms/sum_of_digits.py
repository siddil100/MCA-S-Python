num=int(input("enter number: "))
sum=0
while(num>0):
    m=num%10
    sum=sum+m
    num=num//10
print(sum)

