import copy


x3 = float(input('Digite o coeficiente de x^3: '))
x2 = float(input('Digite o coeficiente de x^2: '))
x1 = float(input('Digite o coeficiente de x^1: '))
i = float(input('Digite o termo idependente: '))
epsilon = float(input('Digite o epsilon: '))
lista_de_valores = []


for interacao in range(-10, 11):
    fdx = (interacao**3)*x3 + (interacao**2)*x2 + interacao*x1 + i
    fdx_1 = ((interacao+1)**3)*x3 + ((interacao+1)**2)*x2 + \
        (interacao+1)*x1 + i
    print(f'Para x = {interacao}, f(x) = {fdx}')
    sinal = fdx / abs(fdx)
    if sinal != fdx_1 / abs(fdx_1):
        lista_de_valores.append((interacao, interacao+1))


print(lista_de_valores)

valorA = copy.deepcopy(lista_de_valores[0][0])
valorB = copy.deepcopy(lista_de_valores[0][1])
while abs(valorB - valorA) > epsilon:
    print('Vamos calcular os zero da função que estão'
          f'no {valorA} e {valorB}')
    ponto_medio = float((valorA + valorB)/2)
    fdx = (ponto_medio**3)*x3 + (ponto_medio**2)*x2 + ponto_medio*x1 + i
    if fdx >= 0:
        valorB = float(ponto_medio)
    else:
        valorA = float(ponto_medio)
print(f'O zero da função está em {ponto_medio:.10f}')
