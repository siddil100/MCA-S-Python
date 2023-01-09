rows= int(input("Please enter the number of rows : "))
for i in range(1, rows + 1):
    for j in range(1, i + 1):
                                        # For printing the multiplication of row to column, we use the formula i*j as below
        print(i * j, end='  ')
    print()