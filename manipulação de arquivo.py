#dentro do open eu também posso adicionar o endereço de onde eu quero armazenar meu arquivo.
#o 'w' é utilizado para a escrita de um arquivo NOVO, caso queira escrever algo em um arquivo já existente, utilizamos 'a'
#aqui eu criei dois métodos, um com 'w' para escrever o arquivo e o outro com 'a' para 'editar' o arquivo
def escrever_arquivo(texto):
    arquivo = open('teste.py', 'w')
    arquivo.write(texto)
    arquivo.close()

def acrescentar(texto):
    arquivo = open('teste.py', 'a') 
    arquivo.write(texto)
    arquivo.close()

#Aqui temos um método para a leitura de um arquivo utilizando o 'r' de read.
def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)

#Aqui eu chamo os métodos dentro da main, pois se eu quiser utilizá-los em outros algoritimos, não terei problemas.
if __name__ == '__main__':
    #escrever_arquivo('print("Hello World")')
    #acrescentar('\nprint("Adele cantora da geracao")')
    ler_arquivo('teste.py')
