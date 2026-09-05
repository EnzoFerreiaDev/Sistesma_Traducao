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
            nome_digitado = (input('Digite o nome da conta:')).strip()
            for conta in contas:
                if nome_digitado.lower == conta.nome.lower:
                    aux = True
            if not nome_digitado:
                print('O nome nao pode ficar vazio.')

           #Verifica se tem conta com o mesmo nome.
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
        nome_login = (input('digite o Nome da Conta: ')).strip()
        senha_login = (input('Digite sua Senha: '))

        for conta in contas:
            if nome_login.lower == conta.nome.lower and senha_login == conta.senha:
                logado = True
                conta_logada = conta
                break

        if logado:
            print('-------------------')
            print('Acesso Liberado!')
            print(f'Bem-vindo: {conta_logada.nome}')
            print('-------------------')
        else:
            print('-------------------')
            print('Acesso Negado!')
            print('Senha ou nome incorretos.')
            print('-------------------')

    if opcao == 3:
        if  logado:
            print('-------------------')
            print('Acesso Liberado!')
            print('-------------------')
            print()

            print('---Area de Deposito---')

            try:

                valor_deposito = float(input('Digite um Valor para deposito R$: '))

                if valor_deposito <= 0:
                    print('Digite um valor maior que zero!')

                conta_logada.saldo += valor_deposito
                print()
                print('-----------------')
                print(f'Deposito Realizado: {valor_deposito:.2f}')
                print(f'Saldo Atual:  {conta_logada.saldo:.2f}')
                print('-----------------')

            except ValueError:
                print('Digite um valor Valido!')
            
        else:
            print('-------------------')
            print('Acesso Negado!')
            print('Faça login primeiro!')
            print('-------------------')

    if opcao == 4:
        if logado:
             print('-------------------')
             print('Acesso Liberado!')
             print('-------------------')
             print()
             try:
        
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
             except ValueError:
                 print('Digite um valor valido!')

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
            print('--- Consulta de Saldo ---')
            print(f'Titular: {conta_logada.nome}')
            print(f'conta: {conta_logada.numero}')
            print(f'Saldo Atual R$: {conta_logada.saldo:.2f}')
        else:
             print('-------------------')
             print('Acesso Negado!')
             print('Faca login primeiro')
             print('-------------------')

    if opcao == 6:
        print('Saindo do Sistema......')
        print('Obrigado por utilizar o Banco!')

    if opcao == 7:

        if conta_logada is None:
            print('Nenhuma conta Logada.')

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
            print('Faca login primeiro')
            print('-------------------')

            
