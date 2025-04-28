# Funções auxiliares

def agendar_modelo(marca): # Selecionando modelos
    print(f"\nModelos disponíveis para {marca}:")
   
    if marca == "fiat":
        print("1 - Argo\n2 - Pulse\n3 - Toro")

    elif marca == "Ford":
        print("1 - Ka\n2 - Fiesta\n3 - Ranger\n")

    elif marca == "Chevrolet":
        print("1 - Onix\n2 - Tracker\n3 - S10\n")

    elif marca == "Volksvagen":
        print("1 - Polo\n2 - Tcross\n3 - Nivus\n")

    modelo = input("Escolha o modelo (1, 2, 3): ")
    data = input("Digite a data para retirada (DD / MM / AAAA): ")
    print(f"Veículo agendado com sucesso para o dia {data}!\n")


def falar_com_atendente():
    opcao_3 = int(input("\nDigite a opção: \n1 - Dúvidas\n2 - Financeiro\n3 - Sinistro"))

    if opcao_3 == 1:
        mensagem = input("Envie uma mensagem: ")
        print("Mensagem enviada com sucesso! Em breve responderemos.\n")

    elif opcao_3 == 2:
        opcao_4 = int(input("\nDigite a opção:\n1 - Solicitar reembolso\n2 - Solicitar estorno cartão\n3 - Confirmação de pagamento\n"))

        if opcao_4 == 1:
            print("Reembolso em análise, aguarde a confimação!")

        elif opcao_4 == 2:
            print("Estorno em análise, aguarde a confimação!")

        elif opcao_4 ==3:
            data_pagamento = input("Informe a data do pagamento (DD / MM / AAAA): ")
            print("Iremos verificar seu pagamento!\n")

        else:
            print("Opção invalida. Digite novamente!")

    elif opcao_3 == 3:
        contrato = input("Digite seu contrato: ")
        print("Um atendente irá entrar em contato!\n")

    else:
        print("Opção invalida. Digite novamente!")



# Página inicial do programa.

print("=== Bem-vindo à LocaPE! ===")
nome = input("Digite seu nome: ")
cpf = input("Digite seu CPF: ")

print(f"\nOlá, {nome}! Seja bem-vindo(a).")

# Menu de opções

print("\nO que deseja fazer?")

opcao = int(input("Digite a opção abaixo: \n1 - Agendar retirada do veículo: \n2 - Entrega do veículo: \n3 - Falar com atendente:\n"))

if opcao == 1: ## Agendar retirada do veículo escolhendo marca e modelo.

   marca_opcao = int(input("\nSelecione a marca do veículo:\n1 - Fiat\n2 - Ford\n3 - Chevrolet\n4 - Volksvagen\n"))

   marcas = {1: "fiat", 2: "Ford", 3: "Chevrolet", 4: "Volksvagen"}

   if marca_opcao in marcas:
       agendar_modelo(marcas[marca_opcao])

   else:
       print("Opção invalida. Digite novamente!")

elif opcao == 2:

    data_entrega = int(input("\nDigite o dia de entrega do veículo (DD / MM / AAAA): "))
    print("Horário de entrega até as 22:00h.\n")

elif opcao == 3:
    falar_com_atendente()
   

else:
    print("Opção invalida. Digite novamente!")