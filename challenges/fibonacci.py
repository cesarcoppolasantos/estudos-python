def fibonacci(range):

    term_a = 0  # Variável que recebe o termo A da sequência de Fibonacci, sempre começando em 0
    term_b = 1  # Variável que recebe o termo B da sequência de Fibonacci, sempre começando em 1
    temp = 0  # Variável que armazena temporariamente o resultado do termo A da sequência de Fibonacci

    fibonacci_sequence = []  # Array que armazena toda a sequência de Fibonacci gerada

    while term_a <= range:

        fibonacci_sequence.append(term_a)  # Armazena o resultado atual da sequência de Fibonacci no array fibonacci_sequence

        temp = term_a  # A variável temp armazena temporariamente o resultado do termo A da sequência de Fibonacci

        term_a += term_b  # O termo A é adicionado ao termo B da sequência de Fibonacci

        term_b = temp  # Após adicionar o termo A ao termo B, a variável term B recebe o valor armazenado na variável temp

    print(fibonacci_sequence)  # Imprime a sequência de Fibonacci gerada

    return fibonacci_sequence  # Retorna o resultado da sequência de Fibonacci como um array


def main():
    fibonacci(200)


if __name__ == "__main__":
    main()
