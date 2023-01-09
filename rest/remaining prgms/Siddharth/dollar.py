mylist=[]
while(True):
   val = eval(input("enter the string to be inserted to list in quotes: "))
   mylist.append(val)
   choice = input("Type yes to stop INSERTING else other keys: ")
   if (choice == "yes"):
      break
str1=mylist[0]
char = str1[0]
str1 = str1.replace(char,'$')
str1 = char + str1[1:]
print(str1)