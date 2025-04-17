# Faça um algoritmo que leia o salário de um fucionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Qaul é o salário do Funvionário? R$:'))
novo = salario + (salario * 15 / 100)
print('Um fucionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R$:{:.2f}'.format(salario, novo))