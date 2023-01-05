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
