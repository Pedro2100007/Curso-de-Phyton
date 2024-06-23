num = 0
d0a25 = 0
d26a50 = 0
d51a75 = 0
d76a100 = 0

while num >= 0:
    num = int(input("valor "))

    if num > 0:
        if num <= 25:
            d0a25 += 1
        else:
            if num <= 50:
                d26a50 += 1
            else:
                if num <= 75:
                    d51a75 += 1
                else:
                    if num <= 100:
                        d76a100 +=1

print(d0a25)
print(d26a50)
print(d51a75)
print(d76a100)