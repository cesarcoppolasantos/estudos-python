"""
    push - append
    pop - pop
    top - stack[n-1]
    empty - True or False
"""


stack = [

]

empty = None

for i in range(1, 11):
    stack.append(i)
    
    print(f'{stack} - Stack top: {stack[i-1]}')

while len(stack) != 0:

    try:
        last_element_removed = stack.pop()

        print(f'\nLast element removed: {last_element_removed}')

        print(f'\n{stack} - Stack top: {stack[len(stack)-1]}')

    except IndexError:

        empty = True

else:
    empty = True

print(f'\nStack is empty: {empty}')
