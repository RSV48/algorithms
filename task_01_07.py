# По длинам трех отрезков, введенных пользователем, определить возможность существования треугольника,
# составленного из этих отрезков. Если такой треугольник существует, то определить,
# является ли он разносторонним, равнобедренным или равносторонним.

a, b, c = input('Ввведите через пробел длины сторон треугольника (a b c): ').split()
a = float(a)
b = float(b)
c = float(c)
if a + b > c and a + c > b and c + b > a:
    if a == b == c:
        print('Треугольник равносторонний')
    elif a != b != c:
        print('Треугольник разносторонний')
    else:
        print('Треугольник равнобедренный')
else:
    print('Треугольник не существует')
