nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
qtd_letras = len(nome)


if nome and idade:

    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]} ')
    if '' in nome:
        print('Seu nome contém espaços')
    else:
        print('Seu nome não contém espaços')
        
    print(f'Seu nome tem {qtd_letras} letras')
    print(f'A ultima letra do seu nome é {nome[-1]}')

else:
    print('Você deixou campos vazios')