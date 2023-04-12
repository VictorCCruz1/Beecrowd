x =(input().split())
a = float(x[0])
b = float(x[1])
c = float(x[2])
delta = (b**2) - 4*a*c
if  delta > 0 and a != 0:
    x1 = (-b + (delta)**(1/2)) / (2*a)
    x2 = (-b - (delta)**(1/2)) / (2*a)
    print('R1 = {:.5f}'.format(x1))
    print('R2 = {:.5f}'.format(x2))
else:
    print('Impossivel calcular')