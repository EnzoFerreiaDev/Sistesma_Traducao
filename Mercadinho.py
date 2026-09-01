class Produto:
    def __init__(self ,nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

produtos = []
opcao = None

while opcao != 7:
    print('---Bem-Vindo ao Mercadinho!---')
    print('Escolha uma das opcoes abaixo:')
    print('[1] - Cadastrar Produto')
    print('[2] - Listar Produtos')
    print('[3] - Pesquisar Produto')
    print('[4] - Ordenar Produtos')
    print('[5] - Mais Caro')
    print('[6] - Mais Barato')    
    print('[7] - sair')
    opcao = int(input('Digite aqui: '))

    if opcao == 1:
        if len(produtos) < 10:
         nome = str(input('Digite o Nome do Produto: '))

         while True:
            try:
                preco = float(input('Digite o Preço do Produto: '))
                break
            except ValueError:
                print('Digite um Valor valido!')

         while True:
            try:
               quantidade = int(input('Digite a Quantidade do Produto: '))
               break
            except ValueError:
                print('Digite uma Quantidade Valida!')

         novo = Produto(nome, preco, quantidade)
         produtos.append(novo)

        else:
            print('Cadasttro Invalido! Limite Alcançado')


    elif opcao == 2:
        for produto in produtos:
            print(f'Nome: {produto.nome}')
            print(f'Preço: {produto.preco}')
            print(f'Quantidade: {produto.quantidade}')
            print('---------------------------------')

    elif opcao == 3:
        achou = False
        encontrado = None

        busca = str(input('Digite o  Nome do Produto para Busca: '))

        for i, produto in enumerate(produtos):
            if produto.nome == busca:
                achou = True
                encontrado = i

        if achou:
            print('---------------------')
            print('Produto Encontrado!')
            print(f'Nome: {produtos[encontrado].nome}')
            print(f'Preço: {produtos[encontrado].preco}')
            print(f'Quantidade: {produtos[encontrado].quantidade}')
            print('---------------------')  
        else:
            print('Produto nao Encontrado') 

    elif opcao == 4:
        for i in range(1, len(produtos)):
            chave = produtos[i]
            j = i - 1
            while j >= 0 and produtos[j].preco > chave.preco:
                produtos[j +1] = produtos[j]
                j += -1
            produtos[j + 1] = chave
        print('Produtos Ordenados!')


    elif opcao == 5:
        mais_caro = 0
        for i in range(1, len(produtos)):
            if produtos[i].preco > produtos[mais_caro].preco:
                Maiscaro = i

        print('---Produtos mais Caros Listados---')
        print(f'Nome {produtos[mais_caro].nome}')
        print(f'Preco: {produtos[mais_caro].preco}')
        print(f'Quantidade: {produtos[mais_caro].quantidade}')
        print('----------------------------------')

    elif opcao == 6:
        mais_barato = 0
        for i in range(1, len(produtos)):
            if produtos[i].preco < produtos[mais_barato].preco:
                mais_barato = i

        print('---Produtos mais Baratos Listados---')
        print(f'Nome: {produtos[mais_barato].nome}')
        print(f'Preco: {produtos[mais_barato].preco}')
        print(f'Quantidade: {produtos[mais_barato].quantidade}')
        print('------------------------------------')

    elif opcao == 7:
        print('Saindo...')
    else:
        print('Opcao Invalida!')
      
