#Utilizando init para instanciar

class Calculadora:
  def __init__(self, num1, num2):
    self.a = num1
    self.b = num2

  def soma(self):
    return self.a + self.b

  def sub(self):
    return self.a - self.b

  def mult(self):
    return self.a * self.b

  def div(self):
    return self.a / self.b

calculadora = Calculadora(10, 2)
print(calculadora.soma())
print(calculadora.sub())
print(calculadora.mult())
print(calculadora.div())

#sem utilizar o init

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
print(calculadora.soma(1, 2))
print(calculadora.sub(2, 3))
print(calculadora.mult(4, 5))
print(calculadora.div(3, 2))
