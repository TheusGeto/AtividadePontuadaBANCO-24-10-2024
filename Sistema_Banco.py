import os

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_menu(): 
    limpar_terminal()
    print("\nMENU")
    print("1 - SALDO")
    print("2 - SAQUE")
    print("3 - DEPOSITO")
    print("4 - TRANSFERENCIA")
    print("5 - CONSULTA DE RENDIMENTO")
    print("0 - SAIR...")
    opcao = int(input("Digite uma opção: "))  # Corrigido
    return opcao  # Adicionado retorno da opção

def verificar_banco(banco):
    return banco.lower() == "caixa"

def verificar_nome(nome):
    return nome == "Matheus Gabriel"

def verificar_senha(senha):
    return senha == "caixa@1234"

def exibir_saldo(saldo):
    print(f"Seu saldo atual é R${saldo:.2f}")

def realizar_saque(saldo):
    valor = float(input("Digite o valor do saque: "))
    if valor <= saldo:
        saldo -= valor
        print("}}}} Saque efetuado com sucesso {{{{")
        print(f"Seu novo saldo é R${saldo:.2f}")
    else:
        print("****SALDO INSUFICIENTE****")
    return saldo

def realizar_transferencia(saldo):
    valor = float(input("Digite o valor da transferência: "))
    if valor <= saldo:
        saldo -= valor
        print("}}}} Transferência efetuada com sucesso {{{{")
        print(f"Seu novo saldo é R${saldo:.2f}")
    else:
        print("****SALDO INSUFICIENTE****")
    return saldo

def realizar_deposito(saldo):
    valor = float(input("Digite o valor do depósito: "))
    conta = input("Digite o número da conta: ")
    agencia = input("Digite sua agência: ")
    confirmar = int(input(f"Confirma o valor do depósito de R${valor:.2f}? (1: sim, 2: não): "))
    if confirmar == 1:
        saldo += valor
        print("}}}} Depósito efetuado com sucesso {{{{")
        print(f"Seu novo saldo é R${saldo:.2f}")
    return saldo

def consulta_rendimento(saldo):
    taxa_rendimento = 0.005  
    rendimento = saldo * taxa_rendimento
    print(f"O rendimento atual para o seu saldo de R${saldo:.2f} é R${rendimento:.2f}")
    return saldo

def main():
    limpar_terminal()

    banco = input("DIGITE O NOME DO BANCO: ")
    if verificar_banco(banco):
        print("----BEM VINDO AO ATENDIMENTO CAIXA----")
        nome = input("Escreva seu nome: ")
        senha = input("Escreva sua senha: ")
        if verificar_nome(nome) and verificar_senha(senha):
            print("Entrando...")
            saldo = 2100
            continuar = True

            while continuar:
                opcao = mostrar_menu()
                match opcao:
                    case 1:
                        exibir_saldo(saldo)  # Corrigido para não tentar armazenar o retorno
                    case 2:
                        saldo = realizar_saque(saldo)
                    case 3:
                        saldo = realizar_transferencia(saldo)
                    case 4:
                        saldo = realizar_deposito(saldo)
                    case 5:
                        consulta_rendimento(saldo)
                    case 0:
                        print("Saindo")
                        continuar = False
                    case _:
                        print("Opção inválida. Tente novamente.")
        else:
            print("Nome ou senha incorretos.")
    else:
        print("Banco inválido. Esse serviço é válido apenas para o banco Caixa.")

if __name__ == "__main__":
    main()
