def find_it(seq):
    for i in seq:
        count = seq.count(i)
        if count % 2 == 1:
            i = str(i)
            list = i
    return(list)

print(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]))