# Este software aceita 5 entradas e acumula os valores positivos

numero = 0
somatoria = 0

for i in range(5):
    numero = int(input("Valor: "))
    if numero > 0:
        somatoria += numero
else:
    print("Fim do laço")

print("Soma: ", somatoria)
