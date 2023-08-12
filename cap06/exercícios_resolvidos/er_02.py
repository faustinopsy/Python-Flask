poema = 'Soneto de Fidelidade\n\n'
poema += 'De tudo ao meu amor serei atento antes\n'
poema += 'E com tal zelo, e sempre, e tanto\n'
poema += 'Que mesmo em face do maior encanto\n'
poema += 'Dele se encante mais meu pensamento\n\n'
poema += 'Quero vivê-lo em cada vão momento\n'
poema += 'E em seu louvor hei de espalhar meu canto\n'
poema += 'E rir meu riso e derramar meu pranto \n'
poema += 'Ao seu pesar ou seu contentamento \n\n'
poema += 'E assim quando mais tarde me procure \n'
poema += 'Quem sabe a morte, angústia de quem vive \n'
poema += 'Quem sabe a solidão, fim de quem ama \n\n'
poema += 'Eu possa me dizer do amor (que tive): \n'
poema += 'Que não seja imortal, posto que é chama \n'
poema += 'Mas que seja infinito enquanto dure. \n\n'
poema += 'Vinicius de Moraes'
print('\n'*100)
print(poema)
linha = 0
coluna = 0
for letra in poema:
    coluna = coluna + 1
    if letra == '\n':
        coluna = 0
        linha = linha + 1
    if (str.isupper(letra)):
        print("linha: ", linha, "coluna: ", coluna, "letra: ", letra, "Maiuscula")
    else:
        print("linha: ", linha, "coluna: ", coluna, "letra: ", letra)
