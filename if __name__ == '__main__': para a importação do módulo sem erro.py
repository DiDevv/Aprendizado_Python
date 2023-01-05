class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 0
    def power(self):
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True
    def aumentacanal(self):
        self.canal += 1
    def diminuicanal(self):
        self.canal -= 1

#Utilizamos para que o módulo identifique o que precisa ser executado no ambiente principal, para não causar erros de, por exemplo:
#precisarmos comentar ou ignorar todas essas linhas abaixo para não interferir na manipulação das classes.
if __name__ == '__main__':
    televisao = Televisao()
    print('A televisão está ligada: {}'.format(televisao.ligada))
    televisao.power()
    print('A televisão está ligada: {}'.format(televisao.ligada))
    print('Canal: {}'.format(televisao.canal))
    televisao.aumentacanal()
    print('Canal: {}'.format(televisao.canal))
    televisao.aumentacanal()
    print('Canal: {}'.format(televisao.canal))
    televisao.diminuicanal()
    print('Canal: {}'.format(televisao.canal))
