credit_number = "1234-5678-9101-1234"

result1 = credit_number[0]
print(result1)

result2 = credit_number[:4]
print(result2)

result3 = credit_number[5:9]
print(result3)

result4 = credit_number[5:]
print(result4)

result5 = credit_number[-1]
print(result5)

result6 = credit_number[::3]
print(result6)

last_digits = credit_number[-4:]
print(f"xxxx-xxxx-xxxx-{last_digits}")

result = credit_number = credit_number[::-1]
print(result)