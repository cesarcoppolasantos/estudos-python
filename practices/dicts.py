dict = {

}

array = [
    'element 0',
    'element 1',
    'element 2',
    'element 3',
    'element 4'
]

for i, j in enumerate(array):
    dict[str(i)] = f'{j}'

print(dict)


for x in dict:
    print(dict[x])


dict.popitem()

print(dict)


dict.pop('0')

print(dict)


dict.setdefault('new key')

print(dict)


dict.update({'new key': 'element 4'})

print(dict)
