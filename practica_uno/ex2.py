#Programa para identificar números primos
import sys

def Crear_lista(b,n):
  b = 1
  lista_1=[]
  while b<n+1:
    lista_1.append(b)
    b+=1
  return lista_1
  
def primos(lista_suma,n):
  lista_2 = []
  
  for i in range(0,n):
    contador = 0
    for j in lista_suma:
      if i % j == 0:
        contador+=1
    if contador == 2:
      lista_2.append(i)

  return lista_2
  
lim = sys.argv[1]
lim = int(lim)

Primera_lista= Crear_lista(1,lim)
#print(Primera_lista)

Lista_primos = primos(Primera_lista, lim)
print(Lista_primos)