operator = input("Masukkan operator (+ - * /): ")
num1 = float(input("Masukkan nombor pertama: "))
num2 = float(input("Masukkan nombor kedua: "))

if operator == "+":
    result = num1 + num2
    print(round(result, 3))

elif operator == "-":
    result = num1 - num2
    print(round(result, 3))

elif operator == "*":
    result = num1 * num2
    print(round(result, 3))

elif operator == "/":
    result = num1 / num2
    print(round(result, 3))

else:
    print(f"Kau pandai baca kah tidak? Aku suruh kasi masuk operator kenapa kau tidak kasi masuk? {operator} tu apa benda?")