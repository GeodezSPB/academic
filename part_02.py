print("Вычисление периметра и площади прямоугольника.")
strA = input("Ведите длину стороны A, в мм. : ")
strB = input("Ведите длину стороны B, в мм. : ")
a = int(strA); b = int(strB)
r = (a + b) * 2
print("Сторона A =", a,"Сторона B =", b, ": P прямоугольника =", r)
r = a * b
print("Сторона A =", a,"Сторона B =", b, ": S прямоугольника =", r)

print("Вычисление объема и площади куба.")
str = input("Введите длину ребра куба, в мм. : ")
a = int(str)
r = (a * a) * 6
y = a * a * a
print("Длина ребра =", a,"Площадь куба = ", r, "\t Объем равен =", y)
