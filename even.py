def start():
    print ('\033[96m'+'\t\t    (odd/even checker)'+'\033[0m')
    print ('\033[94m','\n\t(1).Start','\033[0m',end='\t')
    print ('\033[94m','\t(2).Exit','\033[0m',end=' ')
    while True:
        star_=input('\n\n\tType(start/exit):').lower()
        if star_=='start':
            num_=int(input('\n\t enter a number:'))
            if (num_ % 2 == 0):
                print (f'\n\tThis is even number: {num_}')
            else:
                print(f'\n\tThis is odd number: {num_}')
            bahar=input('\n\tkya aap bahar nikalna chahte hai(yes/no):').lower()
            if bahar=='yes':
                break
            else:
                continue
        elif star_=='exit':
            print('\n\tThanks!for visiting our app')
            break
        else:
            print('\n\tAapki spelling galat hai!Type kare(start/continue)')
start()
            
    
    
