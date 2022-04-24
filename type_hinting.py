'''
Podemos indicar o tipo do objeto, retorno, variavel.
Porém, não impede que o programa seja executado ou gera erros, caso o tipo não esteja de acordo.
'''

def saudar(nome: str) -> str:
    return f'Oi, {nome}'

print(saudar('Joao'))

