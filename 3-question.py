a = float(input("first side"))
b = float(input("second side"))
c = float(input("third side"))

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("equilateral triangle")
    elif a == b or a == c or b == c:
        print("isosceles triangle")
    elif a != b or a != c or b != c:
        print("scalene triangle")
else:
    print("it's a triangle")