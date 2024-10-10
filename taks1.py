c = int(input('Первый член '))
a = int(input('знаметель '))
n = int(input('количество членов '))
print(c)
for i in range (1,n):
    c*=a
    print(c)
