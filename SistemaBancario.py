account = []
deposit = []
balance = 0

def creatAccount():
    global account, deposit, balance
    name_account = input('Digite o nome da conta: ')
    while name_account in account:
        print('Conta já existente: ')
        name_account = input('Digite o nome da conta: ')
    
    account.append(name_account)
    new_deposit = float(input('Digite o valor do depósito: '))
    while new_deposit <= 0 :
        print('Valor inválido')  
        new_deposit = float(input('Digite o valor do depósito: '))

    deposit.append(new_deposit)
    balance += new_deposit
def lookBalance():
    global balance
    opçao = bool(int(input('Deseje ver o saldo do banco - Sim(1) / Não(0): ')))
    if opçao :
        print('O saldo do banco é R$',balance)

def main():
    opçao = bool(int(input('Deseja ver ou criar um programa (1) ou fechar o programa(0): ')))
    while opçao :
        creatAccount()
        lookBalance()
        opçao = bool(int(input('Deseja ver ou criar um programa (1) ou fechar o programa(0): ')))

main()