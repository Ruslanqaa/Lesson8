a = int(input('Введите число a: '))
b = int(input('Введите число b: '))
c = int(input('Введите число c: '))
if a == b and b == c:
    print(3)
elif a == b or a == c or b == c:
    print(2)
elif a != b and b != c:
    print(0)