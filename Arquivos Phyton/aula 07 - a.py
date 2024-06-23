def numerosAleatorios():
    print(1)
    print(3)
    print(18)
    print("dentro")

def somaNum(n1,n2):
    soma=n1+n2
    print("a soma dos dois números é {}, seu orêia!".format(soma))
    return(soma)

print ("antes")
numerosAleatorios()
print ("depois")

somaNum(3,7)
resultado = somaNum(10,60)
resultado = resultado + 10
print(resultado)