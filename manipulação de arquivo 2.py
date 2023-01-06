#Esse programa escreve um arquivo automaticamente com a nota de quantos alunos você quiser, ele também retorna a média desses alunos.
#OBS: QUEBREI MUITO A CABEÇA FAZENDOOOOOOOOoooo
def escrever_arquivo(nome_arquivo, texto):
    arquivo = open(nome_arquivo, 'a')
    arquivo.write(texto)
    arquivo.close()


def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)


def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    nota_aluno = arquivo.read()
    nota_aluno = nota_aluno.split('\n')
    for x in nota_aluno:
        lista_notas = x.split(',')
        aluno = lista_notas.pop(0)
        soma_notas = 0
        n_notas = 0
        for x in lista_notas:
            nota = float(x)
            soma_notas += nota
            n_notas += 1
            media = soma_notas / n_notas

    print('A média de {} é: %.2f'.format(aluno) % (media))
        

if __name__ == '__main__':
    a = int(input('Quantos alunos deseja adicionar?: '))
    for x in range(0, a):
        aluno = input('Nome e nota:')
        escrever_arquivo('Notas.py', '{}\n'.format(aluno))
        media_notas('Notas.py')
