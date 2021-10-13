# Este software aceita 5 entradas e acumula os valores positivos
# Mas se for digitado 1000, interrompe a contagem

numero = 0
somatoria = 0

for i in range(5):
    numero = int(input("Valor: "))
    if numero > 0:
        somatoria += numero
    if  numero == 1000:
        break
else:
    print("Fim do laço")

print("Soma: ", somatoria)
