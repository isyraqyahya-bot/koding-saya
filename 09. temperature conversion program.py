unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
temp = float(input("Enter the temperature: "))

if unit == "C":
    temp = round((temp * 9 / 5) + 32, 0)
    print(f"The temperature in Fahrenheit is: {temp}F.")

elif unit == "F":
    temp = round((temp - 32) * 5 / 9, 0)
    print(f"The temperature in Celsius is: {temp}C")

else:
    print(f"{unit} is an invalid of measurement.")