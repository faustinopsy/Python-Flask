string_original = "Ser ou não ser, eis a questão."
print('A string original é %s' % string_original)
print('Acessando a funçao como um metodo da classe string:')
print('Centralizada em 40 colunas: %s' % str.center(string_original, 40))
print('Centralizada em 40 colunas entre *: %s' % str.center(string_original, 40, '*'))
print('Acessando a funçao a partir do proprio objeto:')
print('Centralizada em 40 colunas: %s' % string_original.center(40))
print('Centralizada em 40 colunas entre *: %s' % string_original.center(40, '*'))
