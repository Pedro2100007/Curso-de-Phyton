def verifSetriang(v1,v2,v3):
    if (v1+v2) >= v3 and (v2+v3) >= v1 and (v1+v3) >= v2:
        return 1
    return 0

if verifSetriang(3,2,1) == 1:
    print ("É triângulo")
else:
    print ("NãO É triângulo")