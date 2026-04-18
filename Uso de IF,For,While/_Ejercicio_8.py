a = int(input("Lado 1: "))
b = int(input("Lado 2: "))
c = int(input("Lado 3: "))

if a == b == c:
    print("Equilatero")
elif a == b or b == c or a == c:
    print("Isosceles")
else:
    print("Escaleno")