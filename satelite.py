print("inciso 2")
g=6.67e-11
m=5.97e24
r=6371000
pi=3.1416
T=float(input("ingrese el valor del periodo"))
h=(((g*m*T**2)/3*pi**2)**1/3)-r
print("el valor de la altura es: ",h)
print("inciso 3")
a=86400
b=5400
c=2700
ha=(((g*m*a**2)/3*pi**2)**1/3)-r
hb=(((g*m*b**2)/3*pi**2)**1/3)-r
hc=(((g*m*c**2)/3*pi**2)**1/3)-r
print("la altura para un dia es: ",ha)
print("la altura para 90 min es: ",hb)
print("la altura para 45 min es: ",hc)
print("inciso 4")
e=86.148
he=(((g*m*e**2)/3*pi**2)**1/3)-r
f=ha-he
print("la diferencia de altura es:",f)
