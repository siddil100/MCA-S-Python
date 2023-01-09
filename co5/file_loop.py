#a Python program to read a file line by line and store it into a list.
#  using readlines() this function automatically store it into a list

# without strip()
f=open("clgadd.txt",'r')
file_lines=f.readlines()
print(file_lines)
f.close()

# By using strip()
print("\n File content after removing newline character: ")
mylist=[]
for x in file_lines:
    z=x.strip()
    mylist.append(z)
print(mylist)

f.close()