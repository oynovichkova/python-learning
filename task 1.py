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
    def __init__(self,  x, y, per, squ):
        pass


class Square(Figures):
    def __init__(self, x, y, per, squ):
        pass

f = Round.get_perimetr(1)
print (f)
f = Round.get_centr(2,1)
print (f)
f = Round.get_squ(2)
print (f)
