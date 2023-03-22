#Crie uma função que retorne o maior valor entre dois numeros 
def maior(a,b):
    if a > b:
        return print(f'O maior número é {a}')
    elif b > a:
        return print(f'O maior número é {b}')
    else:
        return print('O números são iguais')
maior(8,8)