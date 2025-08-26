def call():
    numbers=int(input('enter a number:'))
    def num(i):
        if i > numbers:
            return
        else:
            print(i)
    l=1
    while True:
        num(l)
        l += 1
call()    

    