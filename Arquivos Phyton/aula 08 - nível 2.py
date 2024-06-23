#minha solução usando função sort
Vetor = list(range(10))
for i in range (0,10):
    Vetor[i]=int(input("Digite o valor para posição {}: ".format(i)))
print (Vetor)
Vetor.sort()
print (Vetor)


#do curso, porém decrescente (método bubble sort)
nume = list(range(10))
for n in nume:
    nume[n]=int(input("numero para "))
for i in range(0,10):
    for j in range(0,i):
        if n%2 != 0:
            print(nume[i] > nume[j])
            aux = nume[i]
            nume[i] = nume[j]
            nume[j] = aux
print(nume)
