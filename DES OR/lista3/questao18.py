'''18. Faça uma função que recebe, por parâmetro, um valor N e calcula e escreve
a tabuada de 1 até N. Mostre a tabuada na forma:
1 x N = N
2 x N = 2N
...
N x N = N2
'''
def tabuada(n):
    if type(n) != int or n <= 0:
        return Exception

    lista = []
    for c in range(1, n):
        lista.append(n*c)
    return lista

assert tabuada(5) == [5, 10, 15, 20]
assert tabuada(3) == [3, 6]
assert tabuada(-2) == Exception
assert tabuada(0) == Exception
assert tabuada('W') == Exception
print('Todos os testes OK!')
