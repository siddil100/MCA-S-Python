number = int(input("Enter the number: "))
temp = number
reverse = 0
while (number > 0):
    dig = number % 10
    reverse = reverse * 10 + dig
    number = number // 10
if temp == reverse:
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")