# Faça um prograna que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la
# Sabendo que cada litro de tinta, pinta uma área de 2 m².

largura = float(input('Digite sua largura: '))
alt = float(input('Digite sua altura: '))
área = largura * alt
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m²'.format(largura, alt, área))
tinta = área / 2
print('Para pintar essa parede, você precisará de {}L de tinta.'.format(tinta))