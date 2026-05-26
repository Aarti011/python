# Pattern

rows = int(input('Enter the number of rows'))
# outer loop
for i in range(rows):
    # nested loop
    for j in range(i):
        # display number
        print(i, end=' ')
    # new line after each row
    print('')


n=int(input("Enter the no. of rows: "));
for i in range(n):
    for j in range(i):
        print("*", end=" ");
    print("");


m=int(input("Enter the no. of rows: "));
for i in range(m):
    for j in range(i):
        print("#", end=" ");
    print("");
