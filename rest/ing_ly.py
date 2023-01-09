word=input("enter your text: ")
wordcut=word[-3:]
if not("ing" in wordcut):
    text=word+"ing"
    print(text)
else:
    text=word+"ly"
    print(text)