lista=[1,2,3,4,5]

lista2=list(map(lambda N:N**3,lista))
#funcao lambda
def impares (N):
    return N%2==1

def pares (N):
    return N%2==0


lista3= list(filter(impares,lista2))
print(lista3)

lista4= list(filter(pares,lista2))
print(lista4)