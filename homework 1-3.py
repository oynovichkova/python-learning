#4) Пользователь вводит три числа.
# Написать "yes", если можно взять какие-то два из них и в сумме получить третье.

x =int(input())
y =int(input())
z =int(input())

if x+y==z or x+z==y or y+z==x:
    print ('yes')
else:
    print('no')