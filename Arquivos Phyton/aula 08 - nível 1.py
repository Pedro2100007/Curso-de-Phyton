Vetor = [1,2,3,4,5,6,7,8,9,10]
for i in range (0,10):
    Vetor[i]= int(input("Digite o valor para posição {}: ".format(i)))
for n in Vetor:
    if Vetor[n] % 2 != 0:
        print("A posição ",n," do vetor possui número ímpar = ",Vetor[n])
print (Vetor)


nume = list(range(10))
for n in nume:
    nume[n]=int(input("numero para "))
for n in range(0,10):
    if n%2 != 0:
        print(nume[n])
