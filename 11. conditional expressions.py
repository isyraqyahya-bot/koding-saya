num = 2
a = 6
b = 7
age = 25
temperature = 30
user_role = "admin"

print("Positive" if num > 0 else "Negative")
result = "Even" if num % 2 == 0 else "Odd"
print(result)
max_num = a if a > b else b
print(max_num)
min_num = a if a < b else b
print(min_num)
status = "Adult" if age >= 18 else "Minor"
print(status)
weather = "HOT" if temperature > 20 else "COLD"
print(weather)
access_level = "Full Access" if user_role == "admin" else "Limited Access"
print(access_level)