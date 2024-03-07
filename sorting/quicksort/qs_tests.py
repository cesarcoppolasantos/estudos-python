from random import randint
from quicksort import quick_sort


# Função principal
def main():

    """
        Gera arrays aleatórios, os ordena usando o algoritmo quicksort e imprime os arrays antes e depois da ordenação.

        Esta função chama a função random_arrays() para gerar os arrays aleatórios.
        Em seguida, itera sobre esses arrays e os ordena usando o algoritmo quicksort através da função quick_sort().
        Após a ordenação, imprime os arrays antes e depois da ordenação.
    """

    # Chama a função random_arrays para gerar os arrays aleatórios
    arrays = random_arrays()

    # Looping que itera sobre os arrays gerados e os enumera
    for i, j in enumerate(arrays):

        # Imprime o array não ordenado
        print(f"\nInput unsorted array: \n{arrays[i]}")

        # Chama a função quick_sort para ordenar o array atual
        quick_sort(j, 0, len(j)-1)

        # Imprime o array ordenado
        print(f"Output sorted array: \n{arrays[i]}")


# Função que gera arrays aleatórios
def random_arrays():

    """
    Gera 5 arrays aleatórios com tamanhos variáveis entre 1 e 20 elementos.
    Cada elemento é um número aleatório entre 0 e 1000.
    Ao final, retorna uma lista contendo os arrays gerados.
    """

    # Armazena os arrays gerados
    arrays = []

    # Looping que gera 5 arrays
    while len(arrays) < 5:

        # Gera um tamanho aleatório entre 1 e 20 elementos para o array
        array_length = randint(1, 21)
        
        # Gera o array com números aleatórios de 0 a 1000
        arrays.append([randint(0, 1000) for x in range(array_length)])
    
    # Retorna os arrays gerados
    return arrays

# Execução do teste
if __name__ == "__main__":
    main()
