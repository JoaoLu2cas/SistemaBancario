account = []
deposit = []
balance = 0

def creatAccount():
    while True:
        try:
            num_account = input('Digite o número da conta: ')
            num_int = int(num_account)
            break
        except:
            print('Insira apenas números')
            continue
    account.append(num_int)
    make_deposit = input('Digite o valor do primerio depósito: ')
    while True:
        try:
            deposit_float = float(make_deposit)
            break
        except:
            print('Insira apenas números')
            continue
    while deposit_float <= 0 :
        print('Valor inválido')
        try:
            deposit_float = float(make_deposit)
            break
        except:
            print('Insira apenas números')
            continue
    deposit.append(deposit_float)
    balance += deposit_float

def lookBalence():
    opçao = bool(int(input('Deseje ver o saldo do banco - Sim(1) / Não(0): ')))
    if opçao :
        print('O saldo do banco é R$',balance)

def main():
    opçao = (int(input('Deseja ver ou criar um programa (1) ou fechar o programa(0): ')))
    while opçao :
        creatAccount()
        lookBalence()
        opçao = bool(int(input('Deseja ver ou criar um programa (1) ou fechar o programa(0): ')))

main()