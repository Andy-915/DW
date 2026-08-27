

print("1) Triangle\n2) Rectangle\n3) Square\n4) Circle\n5) Quit")


Shape = int(input("Which shape:"))

if Shape == 1:
    Height = float(input("height:"))
    Base = float(input("base:"))
    Area = (Height*Base)/2
    print(f"The area is {Area:.2f}")

elif Shape == 2:
    Length = float(input("length:"))
    Width = float(input("width:"))
    Area = Length*Width
    print(f"The area is {Area:.2f}")

elif Shape == 3:
    Side = float(input("side:"))
    Area = Side **2
    print(f"The area is {Area:.2f}")

elif Shape == 4:
    Radius = float(input("radius:"))
    Area = 3.14*(Radius **2)
    print(f"The area is {Area:.2f}")

elif Shape == 5:
    print("The area of this shape cannot be calculated in this.")
