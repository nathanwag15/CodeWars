def create_phone_number(n):
    if len(n) < 10:
        return("not enough letters")
    return"(" + str(n[0]) + str(n[1]) + str(n[2]) + ") " + str(n[3]) + str(n[4]) + str(n[5]) + "-" + str(n[6]) + str(n[7]) + str(n[8]) + str(n[9])


print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))