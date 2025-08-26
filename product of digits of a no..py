num=int(input('enter any number:'))
def mult_iply(n):
    if n==0:
        return 1
    else:
        return (n%10) * mult_iply(n//10)
print(mult_iply(num))