def main():
    atual = 1
    chamados = []

    while True:
        print("---------ELEVADOR--------")
        print("1 - Chamar elevador")
        print("2 - Processar proximo pedido")
        print("3 - Sair")
        print('--------------------------')
        print(f'Andar atual: {atual}')
        opcao = int(input("Opcao: "))

        if opcao == 1:
            destino = int(input("Digite o andar desejado (1 a 10): "))
            if destino < 1 or destino > 10:
                print("Andar invalido!")
            else:
                chamados.append(destino)
                print("Pedido registrado.")

        elif opcao == 2:
            if len(chamados) == 0:
                print("Nenhum pedido na fila.")
            else:
                destino = chamados[0]
                if destino > atual:
                    print("Subindo...")
                    for i in range(atual + 1, destino + 1):
                        print(f"  -> Andar {i}")
                elif destino < atual:
                    print("Descendo...")
                    for i in range(atual - 1, destino - 1, -1):
                        print(f"  -> Andar {i}")
                else:
                    print("Ja estava neste andar.")

                atual = destino
                print(f"Chegou ao andar {atual}")
                print("*Portas abrindo*")
                chamados.pop(0)

        elif opcao == 3:
            print("Desligando elevador...")
            break

        else:
            print("Opcao invalida")


if __name__ == "__main__":
    main()
  
