a = "Here you can find the perimeter and area of a square and rectangle"
print(a)

e = "The answer will come in cm "
print(e)

b = int(input("Enter the length of one side of the square\n"))

perimeter = (4 * b)
print(f"The perimeter of the square is", perimeter, "cm")

area = (b ** 2)
print(f"The area of the square is", area, "cm")

c = int(input("Enter the length of the rectangle\n"))
d = int(input("Enter the breadth of the rectangle\n"))

peri = (2 * c + d)
print(f"The perimeter of the rectangle is", peri, "cm")

area_2 = (c * d)
print(f"The area of the rectangle is ", area_2, "cm")
