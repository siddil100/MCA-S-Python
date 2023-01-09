mylist=[]
while(True):
   val = eval(input("enter the word to be inserted to list in quotes: "))
   mylist.append(val)
   choice = input("Type yes to stop INSERTING else other keys: ")
   if (choice == "yes"):
      break
max_length = len(mylist[0])
temp = mylist[0]

for element in mylist:
   if(len(element) > max_length):

      max_length = len(element)


print("Length of longest word is ",max_length)