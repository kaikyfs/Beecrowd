v=input().split()
a, b ,c=v
a=float(a)
b=float(b)
c=float(c)
x=(b)**2-4*(a)*(c)
if (a)==0 or x<0:
  print('Impossivel calcular')
else:
  R1=(-(b)+(x**0.5))/(2*(a))
  R2=(-(b)-(x**0.5))/(2*(a))
  print('R1 = {:.5f}'.format(R1)) 
  print('R2 = {:.5f}'.format(R2))