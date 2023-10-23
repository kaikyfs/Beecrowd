a, b, c=(input()).split()
maiorab=(int(a)+int(b)+abs(int(a)-int(b)))/2
maiorabc=(int(maiorab)+int(c)+abs(int(maiorab)-int(c)))/2
print('%d eh o maior'%maiorabc)