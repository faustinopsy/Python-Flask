nomes = ['','','','','']
notas = [0.0, 0.0, 0.0, 0.0, 0.0]
nome = input('Entre com o nome do aluno 1: ')
nota = float(input('Entre com a nota do aluno 1: '))
# Lembre-se: listas são baseadas em *zero*!
nomes[0] = nome
notas[0] = nota
nome = input('Entre com o nome do aluno 2: ')
nota = float(input('Entre com a nota do aluno 2: '))
nomes[1] = nome
notas[1] = nota
nome = input('Entre com o nome do aluno 3: ')
nota = float(input('Entre com a nota do aluno 3: '))
nomes[2] = nome
notas[2] = nota
nome = input('Entre com o nome do aluno 4: ')
nota = float(input('Entre com a nota do aluno 4: '))
nomes[3] = nome
notas[3] = nota
nome = input('Entre com o nome do aluno 5: ')
nota = float(input('Entre com a nota do aluno 5: '))
nomes[4] = nome
notas[4] = nota
media = (notas[0] + notas[1] + notas[2] + notas[3] + notas[4])/5
print(f'A media da turma e {media}')
