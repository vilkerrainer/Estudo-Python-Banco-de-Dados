import keyboard
import time

velocidade = 0
rpm = 0
marcha = 0
aceleracao = 5
desaceleracao = 5
reducao_marcha = 0.1
velocidades_marchas = {0: 0, 1: 80, 2: 150, 3: 220, 4: 300, 5: 400, -1: 40}
rpm_max = 7000

def mostrar_status(velocidade, marcha, rpm):
    marchas_labels = {
        -1: "Ré",
        0: "Neutro",
        1: "1ª Marcha",
        2: "2ª Marcha",
        3: "3ª Marcha",
        4: "4ª Marcha",
        5: "5ª Marcha"
    }
    print(f"\rMarcha: {marchas_labels[marcha]}, Velocidade: {velocidade:.0f} km/h, RPM: {rpm:4d}  ", end="")

def calcular_rpm(velocidade, marcha):
    if marcha == 0:
        return 0
    else:
        return min(int((velocidade / velocidades_marchas[marcha]) * rpm_max), rpm_max)

def calcular_aceleracao(velocidade, marcha):
    max_velocidade = velocidades_marchas[marcha]
    proporcao = velocidade / max_velocidade if max_velocidade > 0 else 0
    if proporcao >= 1:
        return 0
    return aceleracao * (1 - proporcao)

while True:
    if keyboard.is_pressed('w'):
        if marcha != 0 and velocidade < velocidades_marchas[marcha]:
            taxa_aceleracao = calcular_aceleracao(velocidade, marcha)
            velocidade += taxa_aceleracao
            if velocidade > velocidades_marchas[marcha]:
                velocidade = velocidades_marchas[marcha]
        
        if keyboard.is_pressed('right'):
            if marcha < 5:
                velocidade *= (1 - reducao_marcha)
                marcha += 1
                time.sleep(0.3)

        rpm = calcular_rpm(velocidade, marcha)
        mostrar_status(velocidade, marcha, rpm)

    else:
        if velocidade > 0:
            velocidade -= desaceleracao
            if velocidade < 0:
                velocidade = 0
        rpm = calcular_rpm(velocidade, marcha)
        mostrar_status(velocidade, marcha, rpm)

    if keyboard.is_pressed('left'):
        if marcha > -1:
            velocidade *= (1 - reducao_marcha)
            marcha -= 1
            time.sleep(0.3)

        rpm = calcular_rpm(velocidade, marcha)
        mostrar_status(velocidade, marcha, rpm)

    if keyboard.is_pressed('q'):
        print("\nPrograma encerrado.")
        break

    time.sleep(0.1)



# Pressione "w" para acelerar, setinha para direita "->" para aumentar a marcha e setinha para a esquerda "<-" para diminuir a marcha