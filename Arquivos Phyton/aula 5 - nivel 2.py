juros = float(input ("Qual o juros? "))
capital = float(input ("Qual o capital? "))
período = int(input("Qual o período? "))

for i in range(0,período):
    capital = capital + (capital * (juros/100))
    print (capital)2