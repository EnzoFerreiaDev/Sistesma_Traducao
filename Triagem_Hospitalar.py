pacientes = []

print('----------------------')
print('Sistema Posto de Saúde')
print('Olá, Bem-Vindo ao Posto de saúde!')

for i in range(5):
    print('------------------')
    nome = str(input(f'Digite o Nome do Paciente {i}: '))

    while True:
        print('Qual é o Nivel de Atendimento:')
        print('[1] - Urgencia (Vermelho)')
        print('[2] - Urgente (Amarelo)')
        print('[3] - Pouco Urgente (Verde)')
        try:
            nivel = int(input('Digite o Nivel: '))
            if nivel in [1, 2, 3]:
                break
            else:
                print("Nível inválido, digite 1, 2 ou 3.")
        except ValueError:
            print("Digite um número válido.")

    paciente = {'nome': nome, 'nivel': nivel}
    pacientes.append(paciente)

n = len(pacientes)
for i in range(n):
    for j in range(n - i - 1):
        if pacientes[j]['nivel'] > pacientes[j + 1]['nivel']:
            pacientes[j], pacientes[j + 1] = pacientes[j + 1], pacientes[j]

print('-----------------------')
print('Listagem de Atendimento')
for paciente in pacientes:
    print(f'{paciente["nome"]} Nivel: {paciente["nivel"]}')
