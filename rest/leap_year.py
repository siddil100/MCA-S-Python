start = int(input("Enter starting year: "))
end = int(input("Enter ending year: "))

if start < end:
    print ("Here is a list of leap years from ",start," and ",end,":")

while start < end:
    if start % 4 == 0 and start % 100 != 0:
        print(start)
    if start % 100 == 0 and start % 400 == 0:
        print(start)
    start += 1