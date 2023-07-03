import time
import random
import re

#ATRIBUIÇÃO DE CORES E EMOJIS PARA VISUALIZAR MELHOR O CODIGO
cor_padrao = '\033[0m'
cor_verde = '\033[32m'
negrito = '\033[1m'
emoji_ERRO = '\u274C'
emoji_FOGUETE = '\U0001F680'
emoji_planeta_GENERICO = '\U0001fa90'
emoji_expressao_desconfiado = '\U0001F928'
emoji_acerto = '\U0001fa90'
emoji_sol = "\u2600\ufe0f"
emoji_ATENCAO = '\u26A0️'
et = "\U0001F47D"
emoji_terra = '\U0001F30D'
acerto_erro = [emoji_acerto, emoji_ERRO,emoji_terra]

# MURAL INICIAL DO JOGO, VISUAL
def create_starry_mural(width, height):
    mural = [[" " for _ in range(width)] for _ in range(height)]
    chars = ["*", ".", ":"]
    for y in range(height):
        for x in range(width):
            if (
                random.random() < 0.1
            ):
                mural[y][x] = random.choice(chars)
    return mural

def print_mural(mural):
    for row in mural:
        print(" ".join(row))
# Tamanho do mural
mural_width = 80
mural_height = 10
# Criar e imprimir o mural de inicio do joguinho
mural = create_starry_mural(mural_width, mural_height)
print_mural(mural)

#Validação do input do usuário
name_invalid = True
while name_invalid:
    name = input("Digite seu nome pra começar: ")
    def validar_input(texto):
        padrao = r'^[a-zA-Z\s]+$'  # Apenas letras e espaços são permitidos
        if re.match(padrao, texto):
            return True
        else:
            return False
    if validar_input(name):
        name_invalid = False
    else:
        print('Digite um nome válido. Apenas letras e espaços são permitidos.')


# Inicio do Jogo
def texto_digitado_estilo(text, delay=0.009):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()

#TEXTO INICIAL DO JOGO, APRESENTANDO O MAPA E INTERAGINDO COM O JOGADOR
texto_digitado_estilo(f'---- {et} Olá {name.upper()}, você não passou na aula do Marlon e foi mandado para o espaço. {et} ----')
texto_digitado_estilo(f'       Para voltar ao planeta Terra espero que tenha estudado {cor_verde}Introdução a Algoritmo{cor_padrao}\n')
print(f"{negrito}                                       R E G R A S: {cor_padrao}")
print(
    f"{emoji_FOGUETE} ---- Você precisa acertar algumas coordenadas para passar de fase ------------------------ {emoji_FOGUETE}"
)
print(
    f"{emoji_FOGUETE} ---- Cada tentativa errada você perderá uma vida, ao zerar as vidas você {negrito}perde o jogo.{cor_padrao} --- {emoji_FOGUETE}"
)


texto_digitado_estilo(f"{negrito}Vou te mostrar um mapa em formato de {cor_verde}matriz{cor_padrao} e desafiar você a escolher as coordenadas certas para descobrir um planeta.{cor_padrao}")
print()


print(f"""
        Antes de começarmos o jogo, vou te dar uma dica para encontrar o primeiro planeta.
        Desafio você a descobrir quantas iterações serão realizadas na estrutura de repetição abaixo:

        for c in range(1, 7):
        print(c)
        for x in range(1, 6):
        print(x)

        {negrito}Prepare-se para o desafio e tente calcular quantas vezes C e X serão printados.{cor_padrao}"
""")

#Matriz do jogo que será manipulada e escondida do jogador
matriz_escondida = [[0] * 7 for _ in range(7)]
matriz_escondida[0][1] = 1 #Mercúrio - Guilherme
matriz_escondida[1][2] = 2 #Vênus - Guilherme
matriz_escondida[2][5] = 3 #Terra
matriz_escondida[2][3] = 4 #Marte
matriz_escondida[4][2] = 5 #Júpiter - Siqueira
matriz_escondida[4][4] = 6 #Saturno - Siqueira
matriz_escondida[5][3] = 7 #Urano - Cárita
matriz_escondida[6][5] = 8 #Netuno - Cárita
# Matriz que será exibida
matriz = [[f"\u2B1B"] * 7 for _ in range(7)]

# Contadores
tentativas = 0
vidas = [emoji_sol, emoji_sol, emoji_sol]

# While principal do jogo
jogador_vence = 1
while jogador_vence:
    print()
    print('Vidas:'," ".join(vidas))
    print()
    print("   0   1    2   3   4    5   6")  # Exibe os números das colunas e linhas, espaçado pra encaixar no tamanho da nossa matriz de exibição
    for i, linha in enumerate(matriz):
        linha_str = "  ".join(map(str, linha))
        print(f"{i} {linha_str}")
        print()
    print()

    # Jogador escolhe a posição
    posicao = 1
    while posicao:
            linha = input("Linha:  ")
            coluna = input("Coluna: ")

            if not linha.isdigit():
                print("Digite apenas números!")
                continue
            elif not coluna.isdigit():
                print("Digite apenas números!")
                continue
            elif len(linha) != 1 or len(coluna) != 1:
                print("Por favor, digite apenas UM número. \U0001F928")
                continue

            linha = int(linha)
            coluna = int(coluna)

            if 0 <= linha <= 6 and 0 <= coluna <= 6:
                posicao = 0
            else:
                print("\U0001F6D1  Oops, palpite fora do tabuleiro! Tente novamente.  \U0001F6D1\n")


    if matriz[linha][coluna] in acerto_erro:
        print(f"{emoji_ATENCAO}  Você já tentou essa posição!  {emoji_ATENCAO}")
        print()
    elif matriz_escondida[linha][coluna] == 0:
        print(f"Nada encontrado nessa posição... {emoji_ERRO}")
        print()
        matriz[linha][coluna] = emoji_ERRO
        tentativas += 1
        vidas.pop()
    elif matriz_escondida[linha][coluna] == 1:
        matriz[linha][coluna] = emoji_acerto
        texto_digitado_estilo(
            f"\n\U0001fa90   \U0001fa90   \U0001fa90   \033[1m   M   E   R   C   Ú   R   I   O   \033[0m   \U0001fa90   \U0001fa90   \U0001fa90"
        )
        print(
            f"Bem-vindo, {name.upper()}! Estamos em Mercúrio."
        )
        print(f'Prepare-se para enfrentar variações extremas de temperatura em Mercúrio! Durante o dia, a temperatura máxima atinge aproximadamente 425°C, enquanto que a média fica em torno de -60°C. \nDurante a noite, porém, as temperaturas podem despencar para incríveis -180°C.')
        print()

        print(
            f"{negrito}O próximo desafio é sobre tudo que aprendemos em LISTAS na aula do Marlon. Está preparado? Vamos lá ...{cor_padrao}"
        )
        print(
            f"""
                    lista = ['O carro','peixe', 123, 111, 'Introdução', 'Listas']
                    lista.append(124)
                    del lista[1]
                    lista.remove(111)

            {negrito}Para descobrir esse enigma, quantos objetos adicionei e depois retirei da lista?{cor_padrao}"""
        )
    elif matriz_escondida[linha][coluna] == 2:
        matriz[linha][coluna] = emoji_acerto
        texto_digitado_estilo(
            f"\n\U0001fa90   \U0001fa90   \U0001fa90   \033[1m   V   Ê   N   U   S   \033[0m   \U0001fa90   \U0001fa90   \U0001fa90"
        )
        print(
            f"Parabéns {name.upper()},  estamos apenas a 61 milhões de quilômetros de distância da Terra, acredite, sou o mais próximo da Terra."
        )
        print(
            "A rotação de Vênus ocorre de leste para oeste, contrária a todos os planetas do Sistema Solar. Vênus pode ser visto da Terra sem o auxílio de equipamentos.\n"
        )
        print(f"O próximo desafio que você irá fazer é sobre FUNÇÕES usando a linguagem PYTHON. Espero que tenha estudado...\n")
        print(f"""
                    def quociente_resto(x, y):
                      quociente = x // y
                      resto = x % y
                      return (quociente, resto)

                    print('Quociente e resto: ', quociente_resto(17, 6))

              {negrito}Quantos parametros passei na função e qual é o resultado do resto da divisão?{cor_padrao}
        """)
    elif matriz_escondida[linha][coluna] == 3:
        matriz[linha][coluna] = emoji_terra
        texto_digitado_estilo(
            f"\n\U0001F30D   \U0001F30D   \U0001F30D   \033[1m   T   E   R   R   A   \033[0m   \U0001F30D   \U0001F30D   \U0001F30D"
        )
        print(
            f"Parabéns {name.upper()}, você encontrou o planeta Terra. Foi um jornada e tanto em meu amigo, espero que dessa vez você passe na matéria do Marlon!!!\n"
        )
        print(
            "A Terra é o terceiro planeta mais próximo do Sol, o mais denso e o quinto maior dos oito planetas do Sistema Solar. \nÉ também o maior dos quatro planetas telúricos. É por vezes designada como Mundo ou Planeta Azul."
        )
        print()
        break
    elif matriz_escondida[linha][coluna] == 4:
        matriz[linha][coluna] = emoji_acerto
        texto_digitado_estilo(
            f"\n\U0001fa90   \U0001fa90   \U0001fa90   \033[1m   M   A   R   T   E   \033[0m   \U0001fa90   \U0001fa90   \U0001fa90"
        )
        print(
            f"{name.upper()}, chegou em Marte! Se conseguíssemos viajar para a Terra na velocidade da luz, a jornada seria concluída em apenas 14 minutos e 56 segundos."
        )
        print(
            "Marte é um planeta muito frio, árido e rochoso. A sua temperatura máxima é de aproximadamente 25°C, com uma média de -60°C, a qual pode chegar até cerca de -140°C durante à noite."
        )
        print(f'Segue o desafio usando Proposições Lógicas, pois assim você conseguirá chegar ao próximo planeta...'
        )
        print(f"""
                 {cor_verde}Sejam P, Q e R proposições lógicas. Sabendo que P é falsa, P v Q é falsa e P v Q v R é verdadeira, qual o valor lógico de Q e R respectivamente?{cor_padrao}



        """
        )
    elif matriz_escondida[linha][coluna] == 5:
        matriz[linha][coluna] = emoji_acerto
        texto_digitado_estilo(
            f"\n\U0001fa90   \U0001fa90   \U0001fa90   \033[1m   J   Ú   P   I   T   E   R   \033[0m  \U0001fa90   \U0001fa90   \U0001fa90"
        )
        print(
            f"Chegamos em Júpter. Significa que está fazendo um bom trabalho. Parabéns {name.capitalize()}!"
        )
        print('Júpiter é o maior planeta do Sistema Solar, tanto em diâmetro quanto em massa, e é o quinto mais próximo do Sol. \nPossui menos de um milésimo da massa solar, contudo tem 2,5 vezes a massa de todos os outros planetas em conjunto.')
        print()
        print(f"{negrito}O próximo desafio é sobre MATRIZ em PYTHON. Vamos nessa.... Abaixo, quantas matrizes foram criadas e quantos índices cada uma possui?{cor_padrao}")
        print("""

              aula = [[Algoritmo', 'Redes de Computadores', 'Projeto Interdisciplicar], [4, 5, 6], ['faltas', 'revisao', python]]
              notas = [[10, 5, 3.6], [7, 6, 5], [9.6,5,1]]

        """)
    elif matriz_escondida[linha][coluna] == 6:
        matriz[linha][coluna] = emoji_acerto
        texto_digitado_estilo(
            f"\n\U0001fa90   \U0001fa90   \U0001fa90   \033[1m   S   A   T   U   R   N   O   \033[0m  \U0001fa90   \U0001fa90   \U0001fa90"
        )
        print(
            f"    Parabéns {name.capitalize()}, você encontrou Saturno...Será que está fácil demais?!"
        )
        print(
            "Saturno possui 9 vezes o tamanho do planeta Terra e é formado principalmente por gases. Dispõe de 7 conjuntos de anéis circundantes e 82 luas, como Titã, a maior e mais conhecida."
        )
        print("""
                Vamos resolver um exercício que envolve o uso de variáveis. Confira o código abaixo:

                  a = 8
                  b = 10
                  c = 8
                  d = 8

                  soma = (a + b) - (c + d)
        """)
        print(f'{negrito}A quantidade de variavéis te dará a primeira coordenada, e o valor de saída de soma, dará a segunda. Boa sorte, {name.capitalize()}{cor_padrao}.')
    elif matriz_escondida[linha][coluna] == 7:
        matriz[linha][coluna] = emoji_acerto
        texto_digitado_estilo(f'\n\U0001fa90   \U0001fa90   \U0001fa90   \033[1m   U    R    A    N    O   \033[0m   \U0001fa90   \U0001fa90   \U0001fa90')
        print(f'Parabéns {name.upper()}, você encontrou Urano.')
        print(f'Esse desafio vai te levar a um Planeta que tem mais de 80 luas, incluindo a maior delas, chamada Titã.')
        print(f'Será que você se lembra da aula sobre Tabela Verdade? Espero que sim...')
        print(f"""
                p       q       r       ~r     pv~r   q^~r   {negrito}pv~r -> q^~r{cor_padrao}
              | F |   | V |   | V |   | F |   | V |   | F |    {cor_verde}| ? |{cor_padrao}
              | F |   | V |   | F |   | V |   | V |   | V |    {cor_verde}| ? |{cor_padrao}
              | F |   | F |   | V |   | F |   | V |   | F |    {cor_verde}| ? |{cor_padrao}
              | F |   | F |   | F |   | V |   | V |   | F |    {cor_verde}| ? |{cor_padrao}
              | V |   | V |   | V |   | F |   | F |   | F |    {cor_verde}| ? |{cor_padrao}
              | V |   | V |   | F |   | V |   | V |   | V |    {cor_verde}| ? |{cor_padrao}
              | V |   | F |   | V |   | F |   | F |   | F |    {cor_verde}| ? |{cor_padrao}
              | V |   | F |   | F |   | V |   | V |   | F |    {cor_verde}| ? |{cor_padrao}
              """)
        print()
        texto_digitado_estilo(f'{negrito}A soma da quantidade de resultados verdadeiros te dará a próxima coordenada. PS: As duas!!! \U0001F609{cor_padrao}')
        print()
        texto_digitado_estilo(f'Você sabia?  Urano é inclinado em um ângulo de aproximadamente 98 graus.\
        \nEssa inclinação extrema resulta em características únicas, como os polos do planeta recebendo luz solar contínua por 42 anos seguidos e, em seguida, experimentando 42 anos de escuridão contínua. \U0001F62E')
    elif matriz_escondida[linha][coluna] == 8:
        matriz[linha][coluna] = emoji_acerto
        texto_digitado_estilo(f'\n\U0001fa90   \U0001fa90   \U0001fa90  \033[1m  N   E   T   U   N   O  \033[0m  \U0001fa90   \U0001fa90   \U0001fa90\n')
        print(f' Parabéns {name.upper()}, você encontrou Netuno. Mas, ainda está muito muito distante da Terra.\n Posso te ajudar a chegar mais perto.. pra isso aqui está um desafio:  ')
        print()
        texto_digitado_estilo(f' Resolva essa questao e a saída de X e Y te levará a algum lugar. Boa sorte \U0001F609')
        print(f"""{negrito}
            x = 5
            y = 5
            z = 8

            if x >= y:
                x = x - y
            else:
                x = y - z

            if y >= z:
                y = y - z
            else:
                y = z - y

            if z >= (x + y):
                z = z - x - y - 5
            else:
                z = z * x

            print(x, y, z)
        {cor_padrao}""")
        print(f"Você sabia?\nAs temperaturas em Netuno são extremamente frias. Na atmosfera superior, a temperatura pode chegar a cerca de -218 °C, tornando-o um dos lugares mais frios do sistema solar.")
    if tentativas >= 3:
        jogador_vence = 0

if jogador_vence == False:
    print("   0   1    2   3   4    5   6")
    for i, linha in enumerate(matriz):
        linha_str = "  ".join(map(str, linha))
        print(f"{i} {linha_str}")
        print()
    print()

    print('\033[31m' + '                G  A  M  E        O  V  E  R                \n' + '\033[31m')
    print('\033[31m' + '                G  A  M  E        O  V  E  R                \n' + '\033[31m')
    print('\033[31m' + '                G  A  M  E        O  V  E  R                \n' + '\033[31m')
else:

    print(f'{cor_verde}                V  I  T  Ó  R  I  A                {cor_padrao}\n')
    print(f'{cor_verde}                V  I  T  Ó  R  I  A                {cor_padrao}\n')
    print(f'{cor_verde}                V  I  T  Ó  R  I  A                {cor_padrao}\n')
    print()
    print()
    print("   0   1    2   3   4    5   6")
    for i, linha in enumerate(matriz):
        linha_str = "  ".join(map(str, linha))
        print(f"{i} {linha_str}")
        print()
