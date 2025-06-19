

deposito = 0.0
saldo = 0.0
saldo += deposito
saque = 0.0

msg_boas_vindas = "Bem-Vindo ao SantANDRÉ.\n O SEU banco."
msg_menu = "Acesse o menu e escolha o que você irá fazer"
menu = """
    [1] -> Depósito
    [2] -> Saque
    [3] -> Extrato
    [4] -> Avaliar Sistema
    [0] -> Sair

"""
opcao = -1
avalicacao = 0


print(msg_boas_vindas)
print(msg_menu + "\n" + menu)

while True:
    opcao = int(input ("Selecione uma opção do menu: "))
    if(opcao == 1):
        print(f'### DEPÓSITO ###')
        deposito = float(input("Faça o seu depósito: "))
        while(deposito <= 0):
            deposito = float(input("Valor inválido! Insira um número inteiro maior que Zero: "))
        else:
            saldo += deposito
            print("Depósito realizdo com sucesso!")
            print(f'Seu saldo atual é: {saldo}')
            print(menu)
            # opcao = int(input ("Deseja sair ou continuar?\nEscolha uma opção do Menu: "))
            
    elif(opcao == 2):
        saque = float(input("Informe a quantia que deseja sacar: "))
        if(saldo <= 0):
            print ("Saldo insuficiente!")
        else:
            print(f'### SAQUE ###')
            saldo -= saque
            print(f'Saque realizado com sucesso!\nSeu saldo atual é: {saldo}')
            print(menu)
            # opcao = int(input ("Deseja sair ou continuar?\nEscolha uma opção do Menu: "))

    elif(opcao == 3):
        print(f'### EXTRATO ###\nSaldo: {saldo}')
    
    elif(opcao == 4):
        print("### AVALIAÇÃO ###\nEE aí? O que achou do nosso sistema?\nDeixe uma avaliação!")
        avalicacao = int(input("Escolha 0 para muito bom! ou 10 para excelente!: "))
        print(f'Sua escolha foi: {avalicacao}\n Muito obrigado por usar o banco SantANDRÉ')

    elif(opcao == 0):
        print("...Saindo do sistema...")
        print("Muito obrigado por usar o banco SantANDRÉ")
        break


