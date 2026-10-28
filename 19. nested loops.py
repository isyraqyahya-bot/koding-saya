import time

print("Latihan (1)")

rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))
symbol = input("Enter a symbol to use: ")

for a in range(rows):
    for b in range(columns):
        print(symbol, end="")
    print()