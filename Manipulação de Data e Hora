from datetime import date, time, datetime, timedelta

def data():
    data_atual = date.today()
    print(data_atual.strftime('%d/%B/%Y'))
    print(data_atual.strftime('%A'))

def tempo():
    horario = time(hour=15, minute=18, second=30)
    print(horario.strftime('%H:%M:%S'))

def dataEhora():
    data_e_hora = datetime.now()
    print(data_e_hora.strftime('Data: %d/%b/%y  Hora: %H:%M:%S'))
    tupla = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo')
    print(tupla[data_e_hora.weekday()])
    #Diminuindo um ano!
    novadata = data_e_hora - timedelta(days=365)
    print(novadata.strftime('Data: %d/%b/%y  Hora: %H:%M:%S'))

if __name__ == '__main__':
    #data()
    #tempo()
    dataEhora()
