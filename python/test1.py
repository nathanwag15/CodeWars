def duplicate_encode(word):
    word = word.lower()
    new_word = ""
    char_count = {}
    for char in word:
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
    for char in word:
        if char_count[char] > 1:
            new_word += ")"
        else:
            new_word += "("
    return new_word
# print(duplicate_encode("din"))
# print(duplicate_encode("recede"))
# print(duplicate_encode("Success"))
# print(duplicate_encode("(( @"))
print(duplicate_encode("xuk)FJaFRvJk(nx(RPQzzFxn )caQaQkF"))
print(duplicate_encode("kw(dGQdd@e)OvGxbnJnc@SSJIwz(P( "))