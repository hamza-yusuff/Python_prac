def big(num):
    if num==1:
        print('done')
        return 1
    
    else:
        big(num-1)
big(1000)
