print("1")
age = int(input("Enter your age: "))

while age < 0:
    print("Kau belum lahir tu, kasi masuk balik yang betul!")
    age = int(input("Enter your age: "))

print(f"Kau berumur {age} tahun.")

print("2")
name = input("Enter your name: ")

while name == "":
    print("Kasi masuk nama kau bah.")
    name = input("Enter your name: ")

print(f"Hai, {name}")

print("3")
food = input("Enter a food you like (q to quit): ")

while not food == "q":
    print(f"You like {food}.")
    food = input("Enter another food you like (q to quit): ")

print("bye")

print("4")
num = int(input("Enter a number between 1 - 10: "))

while num < 1 or num > 10:
    print(f"{num} is not valid.")
    num = int(input("Enter a number between 1 - 10: "))

print(f"Your number is {num}.")