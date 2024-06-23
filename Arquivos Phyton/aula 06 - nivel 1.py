temp = 0
soma = 0
qtd = 0

while temp != 999:
    temp = float(input("Qual a temp? "))
    if temp != 999:
        soma += temp
        qtd += 1

media = soma / qtd
print(media) 