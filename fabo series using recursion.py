num=int(input('how many series you wanted to print'))
def fab(n):
    if n==0 or n==1:
        return n
    else:
        return fab(n-1)+fab(n-2)
i=0
while i<=num-1:
        print (fab(i),end=' ')
        i+=1
        