import time

print("Latihan (1)")

a_time = int(input("Enter the time in seconds: "))

for a in range(1, a_time):
    print(a)
    time.sleep(1)
print("TIME'S UP!")


print("Latihan (2)")

b_time = int(input("Masukkan nombor lagi: "))

for b in reversed(range(1, b_time)):
    print(b)
    time.sleep(1)
print("SELAMAT TAHUN BARU!!")


print("Latihan (3)") # Ini sama dengan latihan kedua (reversed) tapi dengan cara lain.

c_time = int(input("Masukkan nombor lagi: "))

for c in range(c_time, 0, -1):
    print(c)
    time.sleep(1)
print("SELAMAT TAHUN BARU!")


print("Latihan (4)")

d_time = int(input("Masukkan nombor lagi: "))

for d in range(d_time, 0, -1):
    seconds = d % 60
    minit = int(d / 60) %60  
    jam = int(d / 3600)  
    print(f"{jam}:{minit:02}:{seconds:02}")
    time.sleep(1)
print("SELAMAT TAHUN BARU!")