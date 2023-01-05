import random
taylor = random.randint(1,156)
adele = random.randint(1,157)
#Utilizo o print abaixo como forma de teste para verificar a eficácia do programa
print('taylor:{}, adele:{} '.format(taylor, adele))

a = input("Quem recebeu mais prêmios?")
if taylor > adele and a == 'taylor':
  print('CORRETO!')
elif adele > taylor and a=='adele':
  print('CORRETO!')
else:
  print('Que pena, você ERROU!')
