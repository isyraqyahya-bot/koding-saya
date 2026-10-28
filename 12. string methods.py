name = input("Enter your full name: ")
phone_number = (input("Enter your phone number: "))

result1 = len(name)
print(result1)

result2 = name.find("I")
print(result2)

result3 = name.rfind("m")
print(result3)

result4 = name.capitalize()
print(result4)

result5 = name.upper()
print(result5)

result6 = name.lower()
print(result6)

result7 = name.isdigit()
print(result7)

result8 = name.isalpha()
print(result8)

result9 = phone_number.count("-")
print(result9)

result10 = phone_number.replace("-", " ")
print(result10)

print(help(str))