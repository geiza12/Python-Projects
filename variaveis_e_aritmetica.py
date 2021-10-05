# Uso de variáveis e operações aritméticas simples

#Método 1
x = float(input("Entre com o 1º valor: "))
y = float(input("Entre com o 2º valor: "))
print("A soma dos dois valores digitados é ", (x + y) )

#Método 2
x = float(input("Entre com o 1º valor: "))
y = float(input("Entre com o 2º valor: "))
print("A soma dos valores", x, "e", y, "é", x + y)

#Método 3
x = float(input("Entre com o 1º valor: "))
y = float(input("Entre com o 2º valor: "))
print(f"A soma dos valores {x} e {y} é {x + y} ")

#Método 4
x = float(input("Digite um valor: "))
print("O quadrado de", x, "é", (x*x))

#Método 5 - Formataçãod e casas decimais
soma = 38500   #soma dos salários no ano
media = soma/12.0
# Muitas casas decimais:
print("A média dos salários é ", media)
# Formatação para 2 casas decimais:
print(f"A média dos salários é {media:.{2}f}")
