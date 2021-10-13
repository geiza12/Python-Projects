# Este software aceita 3 entradas e acumula os valores positivos

numero = 0
somatoria = 0
k = 1
while k < 4:
    numero = int(input("Valor: "))
    if numero > 0:
        somatoria += numero
    k = k + 1
    print(k)
print("Soma: ", somatoria)
