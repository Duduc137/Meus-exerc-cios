# Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.

medida = float(input('Uma distancia em metros:'))
cm = medida * 100
mm = medida * 1000
dam = medida* 10
m = medida* 1
dm = medida * 0.1
hm = medida * 100
print('A medida de {} m corresponde a {} cm e {} mm'.format(medida, cm ,mm))
print('A media de {} dam corresponde {} dm e {} hm'.format(medida, dam , dm, hm))
