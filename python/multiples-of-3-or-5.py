def solution(number):
    list = []
    for i in range(number):
        if i != 1 and i != 0:
            if i % 3 == 0 or i % 5 == 0:
                list.append(i)


    return(sum(list))




print(solution(10))
print(solution(200))