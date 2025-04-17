# Crie um programa que leia quantos dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
# considere US$1,00 = R$5.68

real = float(input('Quantos dinheiro você tem na carteira?: R$'))
dolar = real / 5.68
euro = real / 6.13
libra = real / 7.34
print('Com R${:.2f} você pode comprar US${:.2f} EUR${:.2f} GBP${:.2f}'.format(real, dolar, euro, libra))