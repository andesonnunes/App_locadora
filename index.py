## Página inicial do programa.

print("Bem vindo a LocaPE!")
str(input("Digite seu nome: "))
str(input("Digite seu cpf: "))

## Selecionando as opções

opcao = int(input("Digite a opção abaixo: \n1 - Agendar retirada do veículo: \n2 - Entrega do veículo: \n3 - Falar com atendente:\n"))

if opcao == 1: ## Agendar retirada do veículo escolhendo marca e modelo.

    opcao_2 = int(input("Digite a marca do veículo: \n1 - Fiat \n2 - Ford \n3 - Chevrolet \n4 - Volksvagem\n"))

    if opcao_2 == 1: ## Fiat
        int(input("Escolha o modelo: \n1 - Argo \n2 - Pulse \n3 - Toro\n"))
        str(input("Digite a data para retirada (DD / MM / AAAA):\n"))
        print("Veículo agendado com sucesso!")

    elif opcao_2 == 2: ## Ford
        int(input("Escolha o modelo: \n1 - Ka \n2 - Fiesta \n3 - Ranger\n"))
        str(input("Digite a data para retirada (DD / MM / AAAA):\n"))
        print("Veículo agendado com sucesso!")

    elif opcao_2 == 3: ## Chevrolet
        int(input("Escolha o modelo: \n1 - Onix \n2 - Tracker \n3 - S10\n"))
        str(input("Digite a data para retirada (DD / MM / AAAA):\n"))
        print("Veículo agendado com sucesso!")

    elif opcao_2 == 4: ## Volksvagem
       int(input("Escolha o modelo: \n1 - Polo \n2 - Tcross \n3 - Nivus\n"))
       str(input("Digite a data para retirada (DD / MM / AAAA):\n"))
       print("Veículo agendado com sucesso!")

    else: 
        print("Opção invalida. Digite novamente!")

   

elif opcao == 2: ## Entrega do veículo
   
    str(input("Digite o dia para entrega do veículo (DD / MM / AAAA):\n"))
    print("Horário de entrega até as 22:00h")


elif opcao == 3: # Falando com atendente

   opcao_3 = int(input("Digite a opção abaixo:\n1 - Dúvidas \n2 - Financeiro \n3 - Sinistro\n"))

   if opcao_3 == 1: # Dúvidas
       str(input("Envie uma mensagem: "))
       print("Mensagem enviada com sucesso, logo lhe retornaremos!")

   elif opcao_3 == 2: # Financeiro
      
      opcao_4 = int(input("Digite a opção abaixo:\n1 - Solicitar reembolso \n2 - Solicitar estorno cartão \n3 - Confirmação de pagamento\n"))

      if opcao_4 == 1: # Reembolso
          print("Reembolso em análise, aguarde a confimação!")

      elif opcao_4 == 2: # Estorno
          print("Estorno em análise, aguarde a confimação!")

      elif opcao_4 == 3: # Confirmação de pagamento
          str(input("Informe a data do pagamento (DD / MM / AAAA):\n"))
          print("Iremos verificar seu pagamento!")

      else:
           print("Opção invalida. Digite novamente!")

   elif opcao_3 == 3: # Sinistro
       str(input("Digite o número do seu contrato: "))
       print("Um atendente irá entrar em contato!")


else:
    print("Opção invalida. Digite novamente!")