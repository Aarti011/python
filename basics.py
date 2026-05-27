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

# new pattern with numbers
o=int(input("Enter the no. of rows required : "));
for i in range(o,0,-1):
    for j in range(i,0,-1):
        print(i, end=" ");
    print("");
print("DONE")

#pyramid pattern

rows = int(input("Enter the row size for the pattern: "))
for i in range(1, rows + 1):  # Outer loop for rows
    for j in range(rows  - i):  # Inner loop for spaces
        print(" ", end=" ")
    for k in range(1, 2 * i):  # Inner loop for stars
        print("*", end=" ")
    print()
