# Faça um programa que leia algo pelo teclado 
# e mostra na tela o seu tipo primitivo e todas as informaçõas possiveis sobre ele.

a = input('Digite algo:')
print('O tipo primitivo desse valor é ', type(a))
print('Só tem espços? ', a.isspace())
print('É um numeros? ', a.isnumeric())
print('É alfabético? ', a.isalpha())
print('É alfanumérico? ', a.isalnum())
print('Está em maiúsculas? ', a.isupper())
print('Está em minusculas? ', a.islower())
print('Está capitalizada? ', a.istitle())
