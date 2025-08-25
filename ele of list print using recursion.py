def print_list(list,idx=0):
    if idx==len(list):
        return
    else:
        print(list[idx])
    print_list(list,idx+1)
fruits=['apple','banana','litchi','mango']
print_list(fruits)