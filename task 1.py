#1. Реализовать классы: фигура, круг, прямоугольник, квадрат.
# Классы должны предоставлять методы:
#- получение центра
#- получение периметра
#- получение площади

class Figures:
    def __init__(self, name):
        pass

class Round(Figures):
    def __init__(self, name, diam):
        pass
    def get_centr(self):
        pass

    def get_perimetr(self):
        p = 3.14 * int(self)
        return p

    def get_squ(self):
        s = 3.14 * (int(self)/2)**2
        return s

class PramUgol(Figures):
    def __init__(self, name, side_a, side_b):
        pass

    def get_centr(self):
        pass

    def get_perimetr(self):
        pass

    def get_squ(self):
        pass


class Square(Figures):
    def __init__(self, name, side_a):
        pass

    def get_centr(self):
        pass

    def get_perimetr(self):
        pass

    def get_squ(self):
        pass

f = Round.get_perimetr('1')
print (f)

