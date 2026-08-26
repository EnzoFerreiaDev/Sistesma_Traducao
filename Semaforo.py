print('Semaforo Inteligente')

ciclo = 0
estado_atual = 1
Contador = 5

while ciclo < 3:

    match estado_atual:

        case 1:
            print(f'VIA A: verde | VIA B: vermelho - Tempo Restante: {Contador}')
            print()

        case 2:
            print(f'VIA A: amarelo | VIA B: vermelho - Tempo Restante: {Contador}')
            print()

        case 3:
            print(f'VIA A: vermelho | VIA B: verde - Tempo Restante: {Contador}')
            print()

        case 4:
            print(f'VIA A: vermelho | VIA B: amarelo - Tempo Restante: {Contador}')
            print()

        case 5:
            print(f'VIA A: vermelho | VIA B: vermelho - Tempo Restante: {Contador}')
            print()

    # Aqui entraria o Botao se o Prefeito quisesse

    Contador -= 1

    if Contador == 0:
        if estado_atual == 5:
            estado_atual = 1
            ciclo = ciclo + 1
        else:
           estado_atual += 1

        match estado_atual:
                case 1:
                    Contador = 5
                case 2:
                    Contador = 4
                case 3:
                    Contador = 6
                case 4:
                    Contador = 4
                case 5:
                    Contador = 2
                  
