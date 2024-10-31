import os

def limpar_terminal():
    os.system("'cls' if os.name == 'nt' else 'clear'")

def mostrar_menu(): # Exibe o menu de opções e retorna a escolha do usuário
    limpar_terminal()
    print("\nMENU")
    print("1 - SALDO")
    print("2 - SAQUE")
    print("3 - DEPOSITO")
    print("4 - TRANSFERENCIA")
    print("5 - CONSULTA DE RENDIMENTO")
    print("0- SAIR...")
    opçao = int("Digite uma opção: ")

def verificar_banco(banco):# Verificam se as informações batem com as gravadas
    return banco.lower() == "caixa"

def verificar_nome(nome):
    return nome == "Matheus Gabriel"

def verificar_senha(senha):
    return senha == "caixa@1234"

def exibir_saldo(saldo):
    print(f"Seu Saldo atual é R${saldo} ")

#FAZER AQUI DEFs: realizar_saque(saldo), realizar_transferencia(saldo), realizar_deposito(saldo)
def realizar_saque(saldo):
    valor = float(input("digite o valor do saque"))
    if valor <= saldo:
        saldo -= valor
        print("}}}} saque efetuado com sucesso {{{{")
        print(f"seu novo saldo {saldo}")
    else:
        print("****SALDO INSUFICIENTE****")

def realizar_transferencia(saldo):
    valor = float(input("digite o valor da transferencia"))
    if valor <= saldo:
        saldo -= valor
        print("}}}} transferencia efetuada com sucesso {{{{")
        print(f"seu novo saldo {saldo}")
    else:
        print("****SALDO INSUFICIENTE****")

def realizar_deposito(saldo):
    valor = float(input("Digite o valor do deposito: "))
    conta = input("digite o numero da conta: ")
    agencia =  input("Digite sua agencia: ")
    confirmar = int(input(f"confirma o valor do deposito de ${valor} (1: sim, 2: nâo"))
    if confirmar == 1:
        saldo += valor
        print("}}}} deposito efetuado com sucesso {{{{")
        print("seu novo saldo é R$: {saldo}")
    return saldo

def consulta_rendimento(saldo):
    taxa_rendimento = 0.005  
         # Define a taxa de rendimento como 0,5% (ou seja, 0.005).
         # Esse valor representa um rendimento simulado para o saldo.
         # Essa taxa é fixa aqui para simplificar, mas, em uma situação real,
         # poderia variar dependendo do tipo de investimento ou de conta.

    rendimento = saldo * taxa_rendimento
       # Calcula o rendimento esperado multiplicando o saldo pela taxa de rendimento.
       # Por exemplo, se o saldo é R$ 2.100, o rendimento é:
       # 2100 * 0.005 = R$ 10.50.
       # Esse valor representa o ganho que o usuário teria sobre o saldo atual
       # em um período definido, com base na taxa fixa de 0,5%.

    print(f"O Rendimento atual para o seu saldo de R${saldo} é R${rendimento}")
        # Exibe o rendimento calculado ao usuário de forma formatada.
        # A mensagem mostra o saldo atual e o rendimento estimado para facilitar
        # a compreensão do crescimento potencial do saldo com essa taxa.
        # Esse cálculo é ilustrativo e não considera impostos ou taxas adicionais.
    
    return saldo

def main():
    limpar_terminal()

    banco = input("DIGITE O NOME DO BANCO: ")
    if verificar_banco(banco):
        print("----BEM VINDO AO ATENDIMENTO CAIXA----")

        #FINALIZAR A VERIFICAÇAO, E AINDA POR WHILE NO FINALgi