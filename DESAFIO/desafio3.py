a = float(input())
b = float(input())
c = float(input())


#caso o valor seja positvo sera triângulo
if a + b > c and a + c > b and b +c > a:
    print(f'Perimetro = {a + b + c :.1f} ')
else:
    area = ((a + b) * c) / 2
    print(f'Area = {area :.1f}')
