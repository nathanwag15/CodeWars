def is_valid_walk(walk):
    y = 0
    x = 0
    if len(walk) == 10:
        for i in walk:
            print(i)
            if i == 'n':
                y += 1
            elif i == 's':
                y -= 1
            elif i == 'w':
                x -= 1
            elif i == 'e':
                x +=1
            else:
                return 'you have an invalid entry'
        if y == 0 and x == 0:
            return True
        else:
            return False
    else:
        return False

print(is_valid_walk(['n','s','n','s','n','s','n','s','n','s']))