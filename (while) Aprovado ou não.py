nome = input('Nome do Aluno: ')

n1 = float(input('Primeira nota:'))
while n1 > 10:
  print('Nota de zero a dez por gentileza ^^')
  n1 = float(input('Primeira nota:'))

n2 = float(input('Segunda nota:'))
while n2 > 10:
  print('Nota de zero a dez por gentileza ^^')
  n2 = float(input('Segunda nota:'))

n3 = float(input('Terceira nota:'))
while n3 > 10:
  print('Nota de zero a dez por gentileza ^^')
  n3 = float(input('Terceira nota:'))

n4 = float(input('Quarta nota:'))
while n4> 10:
  print('Nota de zero a dez por gentileza ^^')
  n4 = float(input('Quarta nota:'))

media = (n1 + n2 + n3 + n4)/4
print('\nA média de {} é %.2f'.format(nome) % (media))
if media >= 7:
  print('O(a) aluno(a) {} foi APROVADO(a)!'.format(nome))
else:
  print('O(a) aluno(a) {} foi REPROVADO(a)'.format(nome))
