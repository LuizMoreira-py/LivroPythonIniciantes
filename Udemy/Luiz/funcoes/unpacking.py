def soma_2(a, b):
    return a + b


def soma_3(a, b, c):
    return a + b + c


def multiplicar(a, b):
    return a * b


def soma_n(*numeros):
    soma = 0
    for n in numeros:
        soma += n
    return soma


if __name__ == '__main__':
    print(soma_2(7, 7))
    print(soma_3(2, 4, 10))
    print(multiplicar(2, 13))
