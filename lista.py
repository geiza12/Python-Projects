# Crie um programa onde o usuário pode digitar vários valores numéricos e salve-os em uma lista.
# Caso o número já exista na lista, ele não deve ser adicionado.
# No final, serão exibidos todos os valores únicos digitados em ordem crescente.
num = []
continuar = 's'

while continuar == 's':
    valor = int(input('Digite um valor: '))
    if valor not in num:
        num.append(valor)
    else:
        print('Este valor já foi inserido')
    continuar = input('Deseja continuar? (s/n): ')
num.sort()
print(num)
