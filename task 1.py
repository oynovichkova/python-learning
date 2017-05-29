#1. Реализовать классы: фигура, круг, прямоугольник, квадрат.
# Классы должны предоставлять методы:
#- получение центра
#- получение периметра
#- получение площади

class Figures:
    def __init__(self, name, x, y, per, squ):
        pass
    def get_centr(x,y):
        return (x,y)

    def get_perimetr(per):
        return per

    def get_squ(squ):
        return squ

class Round(Figures):
    def __init__(self, name, x, y, per, squ):
        pass

class PramUgol(Figures):
    def __init__(self, name, x, y, per, squ):
        pass


class Square(Figures):
    def __init__(self, name, x, y, per, squ):
        pass

f = Round.get_perimetr(1)
print (f)
f = PramUgol.get_centr(2,3)
print (f)
f = Square.get_squ(4)
print (f)

g = (1,2)
print (g)

