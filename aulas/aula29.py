numero  = input('Vou dobrar o número que vc digitar: ')

# numero_float = float(numero)
# print(f'O dobro de {numero} é {numero_float * 2:.0f}')

try:
    numero_float = float(numero)
    print('FLOAT:', numero)
    print(f'O dobro de {numero} é {numero_float * 2:.0f}')
except:
    print('Isso não é um número')