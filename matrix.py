rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: " ))
matrix = []

for i in range(rows):
    a = []
    for j in range(columns):
        a.append(int(input()))
    matrix.append(a)
print()

for i in range(rows):
    for j in range(columns):
        print(matrix[i][j],end="\t")
    print()
