conjuntoA = {1,2,3,4,5,6}
conjuntoB = {4,5,6,7,8,9}
conjuntoD = {1,3,6,9}
conjuntoE= {3,6}

#1.Escribe un programa en Python que imprima los
#elementos que se encuentran en A o en B, o en ambos.

print(conjuntoA & conjuntoB)

#2. Escribe un programa en Python que imprima los
#elementos que se encuentran en A y en B

conjuntoC = conjuntoA | conjuntoB 
print(conjuntoC)

#3. Escribe un programa en Python que imprima el conjunto 
#de los elementos que se encuentran en A o en B, pero no en ambos.

print(conjuntoA.symmetric_difference(conjuntoB))

#4.Dados un conjunto, A, escribe un programa en Python que imprima si el conjunto es
#un subconjunto de otro conjunto, B.

print(conjuntoA.issubset(conjuntoB)) #no es
print(conjuntoE.issubset(conjuntoE)) #es

#5.Dados un conjunto, A, escribe un programa en Python que imprima el número de
#elementos del conjunto.

print(len(conjuntoA)) #6



