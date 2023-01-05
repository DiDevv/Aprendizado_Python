class Televisao:
  def __init__(self):
    self.ligada = False
    self.canal = 5

  def power(self):
    if self.ligada:
      self.ligada = False
    else:
      self.ligada = True
  
  def aumentacanal(self):
    self.canal += 1
  
  def diminuicanal(self):
    self.canal -= 1


televisao = Televisao()
print('A televisão está ligada: {} '.format(televisao.ligada))
televisao.power()
print('A televisão está ligada: {} '.format(televisao.ligada))
print('Canal: {}'.format(televisao.canal))
televisao.aumentacanal()
print('Canal: {}'.format(televisao.canal))
televisao.diminuicanal()
print('Canal: {}'.format(televisao.canal))



