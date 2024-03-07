string = "roma"

def reverse(string):

    new_string = ""
    
    for i in string[::-1]:
        new_string += i

    return new_string

reversed = reverse(string)

print(reversed)
