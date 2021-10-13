def metodoA(lista):
    lista[0] = 9
    lista[2] = 99

def metodoB(varivelsimples):
    varivelsimples = 88

def metodoC(varivelsimples):
    varivelsimples = "janela"
    
    
minhalista = [4, 2, 3, 6, 7, 8]
metodoA(minhalista)
print(minhalista)

variavelA = 6
metodoB(variavelA)
print(variavelA)

variavelB = "casa"
metodoC(variavelB)
print(variavelB)


# mostrará na tela:
# [9, 2, 99, 6, 7, 8]
# 6
# casa
