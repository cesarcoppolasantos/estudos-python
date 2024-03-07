def array():
    
    """
        Anotações sobre arrays.
    """

    # Array original
    arr = [5, 10, 2, 31] 
    print(f'Array original: \n{arr}')

    # Inverte o array original, mas não o organiza em ordem crescente/decrescente
    arr.reverse() 
    print(f'Array invertido mas não organizado em ordem crescente/decrescente: \n{arr}')

    # Organiza o array em ordem decrescente
    arr.sort(reverse=True) 
    print(f'Array organizado em ordem decrescente: \n{arr}')

    # Organiza o array em ordem crescente
    arr.sort() 
    print(f'Array organizado em ordem crescente: \n{arr}')

    # Adiciona o elemento ao final do array
    arr.append(1) 
    print(f'Array após adicionar um elemento (neste caso, elemento 1) ao final da lista: \n{arr}')

    # Retorna a quantidade de elementos especificados
    count = arr.count(10) 
    print(f'Quantidades de elementos especificados (neste caso, elemento 10): \n{count}')

    # Retorna o índice (começando em 0) do primeiro elemento especificado
    index = arr.index(10)
    print(f'Índice do primeiro elemento especificado (neste caso, 10): \n{index}')

    # Adiciona o elemento especificado na posição de índice especificada
    arr.insert(2, 100) 
    print(f'Array após adicionar o elemento especificado no índice especificado (neste caso, número 100 no índice 2): \n{arr}')

    # Remove o elemento no índice especificado
    arr.pop(2) 
    print(f'Array após remover o elemento no índice especificado (neste caso, índice 2): \n{arr}')

    # Copia um array para outra variável
    new_arr = arr.copy() 
    print(f'O mesmo array em outra variável: \n{new_arr}')
    

if __name__ == "__main__":
    array()
