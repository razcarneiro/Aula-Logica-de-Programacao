#Problema 1 - Valor por hora
# Escreva um programa que retorne o valor hora de um funcionário 
# com base no seu salário mensal e horas trabalhadas por mês.
'''
# Método 5Q's para montar um algorítimo:
Analise criticamente o problema e descubra:
(tente explicar este problema para você mesmo em voz alta e peça mais 
informações/investigue mais até você compeender o problema).

1. Quais são os dados de entrada necessários?
- qual o salário mensal?
- quantidade de horas trabalhadas?

2. Oque deve ser feito com esses dados?
- Calcular o valor hora.

3. Quais são as restrições deste problema?
- Precisa ter um valor do salário mensal.
- Precisa ter um valor da quantidade de horas trabalhadas.

4. Qual é o resultado esperado?
- Exibir o valor hora da pessoa, com base no calcúlo de valor hora.

5.Qual a sequência de passos a ser feita para chegar ao resultado esperado?
(Pseudocódigo)

- Receber o valor do salário mensal.
- Receber o valor da quantidade de horas trabalhadas.
- Calcular o valor hora = salário mensal / quantidade de horas trabalhadas.
- Exibir o valor hora.

'''
salario_mensal = float(input("qual o seu salário mensal?"))
horas_trabalhadas = float(input("quantas horas você trabalha por mês?"))
valor_hora = salario_mensal / int(horas_trabalhadas)
print("O valor hora do funcionário é de R$", valor_hora)