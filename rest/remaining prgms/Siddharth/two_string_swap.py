st=input("enter two strings separated with white spaces: ")
sep=st.split()
mylist=list(sep)
word1=mylist[0]
word2=mylist[1]
fword1=word1[0]
lword1=word1[-1]
midword1=word1[1:-1]
fword2=word2[0]
lword2=word2[-1]
midword2=word2[1:-1]
print(fword2+midword1+lword1+" "+fword1+midword2+lword2)