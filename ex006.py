# Crie um algoritimo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n = int(input('Digite um numero: '))
d = n * 2
t = n * 3
r = n ** (1/2)
print('O Dobro de {} vale {}.'.format(n, d)) #tbm pode ser ('O dobro de {} vale {}'.format(n,(n*2)))
print('O Triplo de {} vale {}.'.format(n, t)) #tbm pode ser('O triplo de {} vale {}'.format(n,(n*3)))
print('A raiz quadrada de {} é igual a {:.2f}.'.format(n, r)) #tbm pode ser ('A raiz quadrada de {} é igual a {:.2f}'.format(n, (1/2)))