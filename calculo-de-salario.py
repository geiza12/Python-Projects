# Cálculo de salário 
# Ler horas trabalhadas no mês 
# Ler o valor para o valor da hora trabalhada
# Ler o percentual de desconto 
# Calcular o salário bruto  ->   SB = HT * VH; 
# Calcular o total de descontos  ->   TD = SB * (PD/100); 
# Calcular o salário líquido  ->   SL = SB – TD; 
# Apresentar os valores de Horas Trabalhadas, Salário Bruto, Total de Desconto e Salário Líquido.
# Thanks Ledón Monstro

HT = float(input('Digite a quantidade de horas trabalhadas: '))
VH = float(input('Digite o valor da hora trabalhada: '))
PD = float(input('Digite o percentual de desconto: '))

# Cálculo do salário bruto (sem descontos)
SB = HT * VH

# Cálculo do total de desconto
TD = SB * (PD/100)

# Cálculo do salário líquido
SL = (SB-TD)
print('\n\nHoras Trabalhadas: ', HT, 'horas')
print('Salário bruto: R$' , round(SB,2))
print('Total de descontos: R$' , round(TD,2))
print('------')
print('Salário líquido: R$' , round(SL,2))
    



