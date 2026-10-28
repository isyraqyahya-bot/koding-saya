weight = float(input("Masukkan berat anda: "))
unit = input("Kilograms atau Pounds (K atau L): ")

if unit == "K":
    weight = weight * 2.205
    unit = "Lbs."
    print(f"Berat kau kalau kita tukar, jadi begini: {round(weight, 2)} {unit}.")

elif unit == "L":
    weight = weight / 2.205
    unit = "Kgs."
    print(f"Berat kau kalau kita tukar, jadi begini: {round(weight, 2)} {unit}.")

else:
    print("Kau mau tau berat kaukah tidak ni?")