def call():
    numbers=int(input('enter a number:'))
    def num(i):
        if i == 0:
            return
        else:
            print(i)
        return num(i-1)
    num(numbers)
call()    

    