""" Resposta de questão 2 dos exercícios propostos do capítulo 12 """
try:
    arquivo = open('abcxyz.txt','r')
    for linha in arquivo:
        print(linha)
except IOError as erro:
    print('Arquivo abcxyz.txt não encontrado.')
    raise
