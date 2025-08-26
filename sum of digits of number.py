num=int(input('enter any number:'))
def sum(i):
    if i==0:
        return 0
    else:
        return (i%10)+sum(i//10)
print(sum(num))       