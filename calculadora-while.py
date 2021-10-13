opc = '+'

while opc=='+' or opc=='*' or opc=='/' or opc=='-' :
    num1 = float(input("Digite um número: "))
    opc = input("Deseja somar, multiplicar, dividir ou subtrair (+ * / -  ou digite . para sair" ) 
    num2 = float(input("Digite outro número: "))
    if opc=='.':
        break;
    if opc=='+':
        soma = num1 + num2
        print("A soma é ", soma)        
    if opc=='*':
        mult = num1 * num2
        print("A multiplicação vale ", mult)
    if opc=='/':
        divid = num1 / num2
        print("A divisão é ", divid)        
    if opc=='-':
        subtr = num1 - num2
        print("A subtração vale ", subtr)

print("Obrigado por utilizar nossa calculadora!")
