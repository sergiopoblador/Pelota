"""Programa para saber numero par e impar"""

print("------------------------")
print("---- numero par---------")
print("------------------------")

# input 
h = int(input("digite la altura inicial: "))
q= h/5
n=0

# processing

while h>q:
    h=h-(0.1*h)
    n=n+1
    print("dio "+ str(n)+" rebotes hasta llegar a su quinta parte de la altura, y su altura fue de "+str(h))

