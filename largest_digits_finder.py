num=int(input('enter any number:'))
lis=[ ] 
while num > 0:
    digit=num%10
    lis.append(digit)
    num//=10
print(max(lis))

        