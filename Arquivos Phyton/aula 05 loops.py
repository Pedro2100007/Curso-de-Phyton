for n in range (0,10):
    print (n, n+1)
    if n > 2:
        print ("n maior 2")
    else:
        print ("n menor 2")

qtda = 0
palavra = input("Digite uma palavra: ")
for letra in palavra:
    print(letra)
    if letra == "a":
            qtda = qtda + 1
print ("quantidade letra a = ", qtda)          