x=input().split()
a, b, c=x
a=float(a)
b=float(b)
c=float(c)
tri=(a*c)/2
cir=3.14159*c**2
trap=(a+b)*c/2
qua=b*b
ret=a*b
print('TRIANGULO: {:.3f}\nCIRCULO: {:.3f}\nTRAPEZIO: {:.3f}\nQUADRADO: {:.3f}\nRETANGULO: {:.3f}'.format(tri,cir,trap,qua,ret))