#2. Пользователь делает вклад в размере n рублей сроком на years лет под 10% годовых
# (каждый год размер его вклада увеличивается на 10%).
# Каждый год пользователь докладывает в банк сумму в  m рублей.
# (Эти деньги прибавляются к сумме вклада, и на них в следующем году
# тоже будут проценты)

#Написать функцию bank, принимающая аргументы n, m и years, и возвращающую сумму,
# которая будет на счету пользователя.

n = int(input())
m = int(input())
y = int(input())

def bank(n, m, y):
        nal = n
        year = y
        def money():
            if year >0:
                nal = n*1.1+m
                year = year -1
                return money()
            else:
                return nal

print (nal)