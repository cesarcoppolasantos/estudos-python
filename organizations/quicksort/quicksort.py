from random import randint


# Função principal do quicksort
def quick_sort(array, left_pointer, right_pointer):

    """
        Quicksort

        Algoritmo de organização eficiente e amplamente utilizado.
        
        Segue a abordagem de dividir para conquistar, dividindo o problema em subproblemas menores
        que são resolvidos independentemente e depois combinados para obter o resultado final.

        A ideia é selecionar um elemento como pivô e dividir o array original em duas partes,
        uma contendo elementos menores que o pivô e outra contendo os elementos maiores que o pivô.

        Após a partição, o algoritmo é aplicado recursivamente nas duas sublistas geradas, até que a lista esteja completamente ordenada.

        Uma vez que todas as sublistas estejam ordenadas, a combinação dessas sublistas resultará na lista ordenada final.

        O ponto chave para a eficiência do quicksort está na escolha do pivô. Um pivô bem escolhido pode reduzir significativamente o tempo de execução do algoritmo.
        O pivô geralmente é escolhido como o primeiro, último ou elemento do meio da lista, 
        mas existem variações do algoritmo que selecionam o pivô de maneira mais inteligente para melhorar o desempenho em diferentes cenários.

        O quicksort possui uma complexidade de tempo média de O(n log n).
        No entanto, em seu pior caso, quando o pivô é mal escolhido e resulta em uma partição desequilibrada,
        a complexidade de tempo pode chegar a O(n^2), embora isso seja raro na prática.
    """

    # Verifica se o array possui apenas um elemento, caso positivo, retorna o array
    if left_pointer == right_pointer:
        return array

    # Inicializa os pointers esquerdo e direito
    i = left_pointer
    j = right_pointer

    # Escolhe um pivô aleatoriamente para evitar casos onde o pivô escolhido é sempre o melhor ou o pior
    pivot_index = randint(left_pointer, right_pointer)
    pivot = array[pivot_index]

    # Looping principal
    while i < j:

        # Avança o ponteiro esquerdo enquanto o elemento for menor que o pivô
        while array[i] < pivot:
            i += 1

        # Retrocede o ponteiro direito enquanto o elemento for maior que o pivô
        while array[j] > pivot:
            j -= 1

        # Se os ponteiros ainda não se cruzaram, faz o swap dos elementos
        if i <= j:
            temp = array[i]
            array[i] = array[j]
            array[j] = temp
            i += 1
            j -= 1

    # Ordena as sublistas recursivamente
    if left_pointer < j:
        quick_sort(array, left_pointer, j)

    if right_pointer > i:
        quick_sort(array, i, right_pointer)
    
    # Retorna o array ordenado
    return array
