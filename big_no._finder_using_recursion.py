lis=[ ]
def count(n):
    if n==0:
        return
    else:
        l=n%10
        lis.append(l)
        return count(n//10)
num=int(input('enter a number:'))
count(num)
print(max(lis))