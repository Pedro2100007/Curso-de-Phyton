def verifSetriang(v1,v2,v3):
    if (v1+v2) >= v3 and (v2+v3) >= v1 and (v1+v3) >= v2:
        return 1
    return 0


def tipoTriang(v1,v2,v3):
    if verifSetriang(v1,v2,v3) == 1:
        if v1==v2 and v2==v3:
            print("Equilátero")
        else:
            if v1!=v2 and v2!=v3 and v1!=v3:
                print("Escaleno")
            else:
                print("Isoceles")]]
    else:
        print ("NãO É triângulo")

lado1 = input("Digite o lado1: ")
lado2 = input("Digite o lado2: ")
lado3 = input("Digite o lado3: ")

tipoTriang(lado1,lado2,lado3)