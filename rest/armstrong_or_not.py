num=int(input("enter a number: "))
orignum=num
result=0
while(orignum!=0):
    remainder=orignum%10
    result=result+remainder*remainder*remainder
    orignum=orignum//10
if result==num:
    print("armstrong")
else:
    print("not armstrong")