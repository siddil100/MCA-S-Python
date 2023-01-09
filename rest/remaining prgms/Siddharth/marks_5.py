#program to enter the name and marks of 5 sub and calculate total and %
sub1n=input("enter the name of first subject ")
sub1m=float(input("Enter the mark of first subject "))
sub2n=input("enter the name of second subject ")
sub2m=float(input("Enter the mark of second subject "))
sub3n=input("enter the name of third subject ")
sub3m=float(input("Enter the mark of third subject "))
sub4n=input("enter the name of fourth subject ")
sub4m=float(input("Enter the mark of fourth subject "))
sub5n=input("enter the name of fifth subject ")
sub5m=float(input("Enter the mark of fifth subject "))
total=sub1m+sub2m+sub3m+sub4m+sub5m
per=total/500*100
print("total is",total,"and percentage is",per,"%")