class Error(Exception):
    pass

class InputError(Error):
    def __init__ (self, message):
        self.message = message
while True:
    try:
        x = int(input('Entre com um número de 0 a 10: '))
        print(x)
        if x > 10 or x < 0:
            raise InputError('O número é inválido pois não pode ser menor que zero e maior que dez')   
        break
    except ValueError:
        print('Valor inválido, deve-se digitar apenas números inteiros.')
