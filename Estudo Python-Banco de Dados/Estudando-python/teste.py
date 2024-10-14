# Aqui terá cálculos matmáticos

#Regra de 3

def regra_de_3():
    valor_inicial = float(input('Se: '))
    x = float(input('É igual a: '))
    y = float(input('Então:'))
    z = float(0)

    z = y*x/valor_inicial

    print(f'Então o resultado é {z}')
    

