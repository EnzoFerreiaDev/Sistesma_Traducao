class Conta:
    def __init__(self ,numero, nome, senha, saldo):
        self.numero = numero
        self.nome = nome
        self.senha =  senha 
        self.saldo = saldo

contas = [] 
logado = False   
opcao = None

while opcao != 6:

    print('---Bem-Vindo ao Sistema Bancario---')
    print('Oque o Senhor(a) Deseja fazer hoje:')
    print('[1] - Criar Conta')
    print('[2] - Login')
    print('[3] - Fazer Deposito')
    print('[4] - Saque')
    print('[5] - Ver Saldo')
    print('[6] - sair')
    print('[7] - Logout')
    while True:
        try:
          opcao = int(input('Digite a opcao: '))
          break
        except ValueError:
            print('Digite uma Opçao Valida!')

    if opcao == 1:
        aux = False
        if len(contas) < 10:
            nome_digitado = str(input('Digite o nome da conta:'))
            for conta in contas:
                if nome_digitado == conta.nome:
                    aux = True

            if aux:
                print('Já existe Conta com esse nome!')
            else:
                senha_digitada = (input('Digite uma Senha: '))
                novo = Conta(numero=len(contas) + 1, nome=nome_digitado, senha=senha_digitada, saldo=0)
                contas.append(novo)
                print('-------------------')
                print('Cadastro Feito')
                print('-------------------')

    if opcao == 2:

        print('----Entrar Na Conta----')
        nome_login = (input('digite o Nome da Conta: '))
        senha_login = (input('Digite sua Senha: '))

        for conta in contas:
            if nome_login == conta.nome and senha_login == conta.senha:
                logado = True
                conta_logada = conta
                break

        if logado:
            print('-------------------')
            print('Acesso Liberado!')
            print('-------------------')
        else:
            print('-------------------')
            print('Acesso Negado!')
            print('-------------------')

    if opcao == 3:
        if  logado:
            print('-------------------')
            print('Acesso Liberado!')
            print('-------------------')
            print()
            print('---Area de Deposito---')
            valor_deposito = float(input('Digite um Valor para deposito: '))
            conta_logada.saldo += valor_deposito
            print()
            print('-----------------')
            print('Deposito Feito')
            print('-----------------')
            
        else:
            print('-------------------')
            print('Acesso Negado!')
            print('-------------------')

    if opcao == 4:
        if logado:
             print('-------------------')
             print('Acesso Liberado!')
             print('-------------------')
             print()
             valor_saque = float(input('Digite o valor para saque: '))
             if valor_saque > conta_logada.saldo:
                 print('------------------')
                 print('Saque Negado!')
                 print('-------------------')
             else:
                 conta_logada.saldo -= valor_saque
                 print('---------------------')
                 print(f'Saque Autorizado, no valor de  {valor_saque}')
                 print('---------------------')
        else:
             print('-------------------')
             print('Acesso Negado!')
             print('-------------------')  

    if opcao == 5:
        if logado:
            print('-------------------')
            print('Acesso Liberado!')
            print('-------------------')
            print()
            print(f'O valor Disponivel em sua conta e: {conta_logada.saldo}')
        else:
             print('-------------------')
             print('Acesso Negado!')
             print('-------------------')

    if opcao == 6:
        print('Saindo do Sistema......')

    if opcao == 7:
        if logado:
            print('-------------------')
            print(f'Voce saiu de: {conta_logada.nome}')
            logado = False
            conta_logada = None
            print('Para entar novamente basta ir em Login')
            print('-------------------')
        else:
            print('-------------------')
            print('Acesso Negado!')
            print('-------------------')
            
