#4. Написать функцию square, принимающую 2 аргумента —
# длину сторон прямогольника, и возвращающую 3 значения:
# периметр, площадь и диагональ прямоугольника.

a = int(input())
b = int(input())
import math

def square(a,b):
    p = 2*(a+b)
    s = a*b
    c = sqrt(a**2 * b**2)
    return p, s, c

print (square(a,b))
