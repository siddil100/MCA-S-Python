mylist=[1,2,3,4,5,6,7,8,9,10]
i=1
l=len(mylist)
while i<=l:
    if i%2==0:
        mylist.remove(i)
    i=i+1
print(mylist)