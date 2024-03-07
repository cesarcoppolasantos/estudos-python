string = "test"


def unique_characters(string):
    temp = []

    for i in string:
        if i not in temp:
            temp.append(i)
        else:
            return False
    
    return True

x = unique_characters(string)

print(x)
