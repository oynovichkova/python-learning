#1. Реализовать классы: фигура, круг, прямоугольник, квадрат.
# Классы должны предоставлять методы:
#- получение центра
#- получение периметра
#- получение площади

class Figures:
    def __init__(self, x, y):
        pass
    def get_centr(x,y):
        return (x,y)

class Round(Figures):
    def __init__(self, x, y, rad):
        super().__init__(x,y)

    def get_perimetr(rad):
        per = rad*2*3.14
        return per

    def get_squ(rad):
        squ = 3.14*rad**2
        return squ

class PramUgol(Figures):
    def __init__(self, x, y, a, b):
        super().__init__(x,y)

    def get_perimetr(a,b):
        per = (a+b)*2
        return per

    def get_squ(a,b):
        squ = a*b
        return squ


class Square(Figures):
    def __init__(self, x, y, a):
        super().__init__(x,y)

    def get_perimetr(a):
        per = 4*a
        return per

    def get_squ(a):
        squ = a**2
        return squ


f = Round.get_perimetr(1)
print (f)
f = Round.get_centr(2,1)
print (f)
f = Round.get_squ(2)
print (f)

f = PramUgol.get_perimetr(1,3)
print (f)
f = PramUgol.get_centr(2,1)
print (f)
f = PramUgol.get_squ(2,3)
print (f)

f = Square.get_perimetr(1)
print (f)
f = Square.get_centr(2,1)
print (f)
f = Square.get_squ(2)
print (f)
