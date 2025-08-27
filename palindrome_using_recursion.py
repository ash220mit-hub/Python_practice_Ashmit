List=[ ]
def reverse(n):
    if n==0:
        return 
    else:
        l=n%10
        List.append(l)
        return reverse(n//10)
num=int(input('\t\tenter any number:'))
reverse(num)
num1=int(''.join(map(str,List)))
if num==num1:
    print (f'yes your number = {num} is palindrome')
else:
    print (f'Sorry your number = {num} is not a palindrome')

