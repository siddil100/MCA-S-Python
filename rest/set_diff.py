color1=input("Enter colours separated by space for colorlist1 :")
color2=input("Enter colours separated by space for colorlist2 :")
sp1=color1.split()
sp2=color2.split()
set1=set(sp1)
set2=set(sp2)
print(set1.difference(set2))