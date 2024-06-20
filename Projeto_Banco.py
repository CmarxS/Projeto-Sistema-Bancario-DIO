menu = """
    ============= MENU =============
    [1] - Depositar
    [2] - Sacar
    [3] - Extrato
    [4] - Sair
    ===============================
"""
print(menu)

escolha = 1

saldo = 0
limite = 500
extrato = " "
limite_diario = 0
saque = ""
deposito = ""

while escolha > 0 :
    escolha = int(input("Escolha uma opção: "))
    if escolha == 1:
        valor_deposito = float(input("Digite o valor do depósito: "))
        saldo += valor_deposito
        deposito += f"Depósito de R${valor_deposito}\n"
        print(f"Depósito de R${valor_deposito} realizado com sucesso!")
    elif escolha == 2: 
        if saldo == 0:
            print("Saldo insuficiente!")
        else:
            valor_saque = float(input("Qual o valor que a ser sacado? "))
            if valor_saque > limite:
                print("Valor acima do limite. Saque inválido!")
            elif limite_diario == 3:
                print("Operação de saque realizada 3 vezes. Volte amanhã!")
            elif valor_saque > saldo:
                print("Saldo insuficiente!")
            else:
                saldo -= valor_saque
                saque += f"Saque de R${valor_saque}\n"
                limite_diario += 1
                print(f"Saque de R${valor_saque} realizado com sucesso! Valor disponível: R${saldo}")
    elif escolha == 3:
        print(f"""
========= Extrato ==========
              
======== Depósitos ========= 
{deposito}
========= Saques ========== 
{saque}
              """)
    elif escolha == 4:
        print("Obrigado por usar nosso serviço, até!")
        break
    else:
        print("Escolha inválida!")