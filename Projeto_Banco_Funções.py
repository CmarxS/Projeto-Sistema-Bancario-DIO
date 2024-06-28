# Atualização do banco utilizando funções
saldo = 0
escolha = 1
limite_diario = 0
limite = 500
extrato = {'saques': [], 'depositos': [], 'saldo': saldo}
cliente = {}
def menu():
    print("""
    ============= MENU =============
    [1] - Depositar
    [2] - Sacar
    [3] - Extrato
    [4] - Cadastrar cliente
    [5] - Cadastrar conta bancária
    [6] - Ver clientes
    [7] - Sair
    ===============================
""")
    escolha = int(input("Escolha uma opção: "))
    if escolha > 6:
        print("Opção inválida!")
    return escolha
def sacar(*, valor_saque):
    global saldo, limite_diario, limite
    if saldo == 0:
        print("Saldo insuficiente!")
    elif valor_saque > limite:
        print("Valor acima do limite. Saque inválido!")
    elif limite_diario == 3:
        print("Operação de saque realizada 3 vezes. Volte amanhã!")
    elif valor_saque > saldo:
        print("Saldo insuficiente!")
    else:
        saldo -= valor_saque
        extrato['saques'].append(f"Saque no valor de: R${valor_saque}")
        limite_diario += 1
        print(f"Saque de R${valor_saque} realizado com sucesso! Valor disponível: R${saldo}")
    return saldo
def depositar(saldo_atual,valor,/ ):
    global saldo
    saldo = saldo_atual + valor
    extrato['depositos'].append(f"Depósito no valor de: R${valor}")
    extrato['saldo'] = saldo
    print(f"Depósito de R${valor} realizado com sucesso!")
    return saldo
def cadastrar_cliente():
    global cliente
    nome = input("Digite o nome do cliente: ")
    cpf = int(input("Digite o CPF do cliente: "))
    data_nascimento = input("Digite a data de nascimento do cliente: ")
    endereco = input("Digite o endereço do cliente: ")
    if cpf in cliente:
        print("CPF já cadastrado!")
    else:
        cliente[cpf] = {'nome': nome, 'data_nascimento': data_nascimento, 'endereco': endereco, 'contas': []}
        print("Cliente cadastrado com sucesso!")
    return cpf

def cadastrar_conta():
    global cliente
    cpf = int(input("Digite o CPF do cliente para vincular a conta: "))
    if cpf in cliente.keys():
        numero_conta = len(cliente[cpf]['contas']) + 1
        conta = f"0001-{numero_conta}"
        cliente[cpf]['contas'].append(conta)
        print(f"Conta cadastrada com sucesso! Número da conta: {conta}")
    else:
        print("CPF não cadastrado. Por favor, cadastre o cliente primeiro.")

def mostra_cliente():
    cpf= int(input("Digite o CPF do cliente: "))
    if cpf in cliente.keys():
        print(f"Nome: {cliente[cpf]['nome']}")
        print(f"Data de nascimento: {cliente[cpf]['data_nascimento']}")
        print(f"Endereço: {cliente[cpf]['endereco']}")
        print(f"Contas: {cliente[cpf]['contas']}")
    else:
        print("CPF não cadastrado.")

def imprimir_extrato():
    print("========= Extrato ==========")
    print(f"O saldo atual é de R${extrato['saldo']}")
    print("======== Depósitos ========")
    print(f"{extrato['depositos']}")
    print("======== Saques =========")
    print(extrato['saques'])

while escolha > 0 :
    escolha = menu()    
    if escolha == 1:
        value = float(input("Digite o valor do depósito: "))
        depositar(saldo, value)
    elif escolha == 2:
        value = float(input("Digite o valor do saque: "))
        sacar(valor_saque = value)
    elif escolha == 3:
        imprimir_extrato()
    elif escolha == 4:
        cadastrar_cliente()
    elif escolha == 5:
        cadastrar_conta()
    elif escolha == 6:
        mostra_cliente()
    elif escolha == 7:
        print("Obrigado por usar nosso serviço, até!")
        break
    else:
        print("Escolha inválida!")