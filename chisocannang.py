a = int(input("Nhap vao can nang:"))
b = float(input("Nhap vao chieu cao:"))
bmi = a/(b*2)

if bmi < 16:
    print("gay cap do III")
elif 16 <= bmi < 17:
    print("gay cap do II")
elif 17 <= bmi <18.5:
    print("gay cap do I")
elif 25 <= bmi < 30:
    print("thua can")
elif 30 <= bmi < 35:
    print("beo phi cap do I")
elif 35 <= bmi < 40:
    print("beo phi cap do II")
else:
    print("Beo phi cap do III")
    
