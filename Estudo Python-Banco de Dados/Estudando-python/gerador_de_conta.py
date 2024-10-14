import string
import random


def gerar_conta():
    caracteres = string.digits
    conta = ''.join(random.choice(caracteres) for i in range(8))
    return conta

conta_banco = gerar_conta()