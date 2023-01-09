start=int(input("Enter the starting range: "))
end=int(input("Enter the ending range "))
squares = [value ** 2 for value in range(start, end + 1)]
print(squares)