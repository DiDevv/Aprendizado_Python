class Calculadora:
    def soma(self, a, b):
        return a + b       
    def sub(self, a, b):
        return a - b
    def mult(self, a, b):
        return a * b
    def div(self, a, b):
        return a / b

calculadora = Calculadora()
print('Soma [1], Subtração[2], Multiplcação[3], Divisão[4]')
op = int(input('Qual operação deseja realizar?: '))

while op < 1 or op > 4:
    print('-------------------------')
    print('Insira um valor válido!')
    print('-------------------------')
    print('Soma [1], Subtração[2], Multiplcação[3], Divisão[4]')
    op = int(input('Qual operação deseja realizar?: '))

if op == 1:
    a = float(input('Insira o primeiro valor:'))
    b = float(input('Insira o segundo valor:'))
    print('O resultado da soma é: {}'.format(calculadora.soma(a, b)))
elif op == 2:
    a = float(input('Insira o primeiro valor:'))
    b = float(input('Insira o segundo valor:'))
    print('O resultado da subtração é: {}'.format(calculadora.sub(a, b)))    
elif op == 3:
    a = float(input('Insira o primeiro valor:'))
    b = float(input('Insira o segundo valor:'))
    print('O resultado da multiplicação é: {}'.format(calculadora.mult(a, b)))
elif op == 4:
    a = float(input('Insira o primeiro valor:'))
    b = float(input('Insira o segundo valor:'))
    print('O resultado da divisão é: {}'.format(calculadora.div(a, b)))
