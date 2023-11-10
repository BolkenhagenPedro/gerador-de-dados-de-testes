from random import choice
from time import sleep
# Função limpar terminal
def limpar_terminal():
    try:
        from os import system
        from platform import system as sys
        
        sistema_operacional = sys()
        
        if sistema_operacional == 'Windows': system('cls')
        elif sistema_operacional == 'Linux': system('clear')
        elif sistema_operacional == 'Darwin': system('clear')

    except:
        return False
        
# Menu
def menu():
    print('Bem-vindo(a) ao menu de Gerador de Dados para Testes, digite "parar" para parar!')
    print('-' * 42)
    print("""Escolha uma ou mais das opções a baixo!
    [1] - Nome
    [2] - Email
    [3] - Telefone
    [4] - Cidade
    [5] - Estado""")

# Entrada de valores
def entrada_de_valores():
    # Loop
    while True:
        limpar_terminal()
        menu()
        resp = input('Informe algum dos valores a cima, separe-os por vírgula sem espaço: ').split(',')
        if resp[0] == 'parar': return False
        # Txt
        txt = input('Gostria de receber os dados em um arquivo txt? [S/N] ').strip().upper()[0]
        while txt not in 'SN':
            print('Digite uma resposta válida!')
            txt = input('Gostria de receber os dados em um arquivo txt? [S/N] ').strip().upper()[0]
                    
        if txt in 'S':
            with open("dados.txt", 'a', newline='') as file:
                try:
                    for resposta in resp:
                        if resposta == '1':
                            nome = um_nome()
                            print(nome)
                            file.write(nome + '\n')
                        elif resposta == '2':
                            email = um_email()
                            print(email)
                            file.write(email + '\n')
                        elif resposta == '3':
                            telefone = um_telefone()
                            print(telefone)
                            file.write(telefone + '\n')
                        elif resposta == '4':
                            cidade = uma_cidade()
                            print(cidade)
                            file.write(cidade + '\n')
                        elif resposta == '5':
                            email = um_email()
                            print(email)
                            file.write(estado + '\n')
                except:
                    print('Erro, você digitou uma opção inválida!')

        elif txt in 'N':
            for resposta in resp:
                if resposta == '1': 
                    nome = um_nome()
                    print(nome)
                elif resposta == '2': 
                    email = um_email()
                    print(email)
                elif resposta == '3': 
                    telefone = um_telefone()   
                    print(telefone)         
                elif resposta == '4': 
                    cidade = uma_cidade()
                    print(cidade) 
                elif resposta == '5': 
                    estado = um_estado()
                    print(estado) 
                else:
                    print('Digite uma opção válida!')
        resp = input('Você deseja gerar outros dados? (S/N) ').strip().upper()[0]
        while resp not in 'SN':
            print('Digite uma resposta válida!')
            resp = input('Você deseja gerar outros dados? (S/N) ').strip().upper()[0]
        if resp == 'N':
            print('Finalizando app...')
            sleep(1.8)
            limpar_terminal()            
            break
        input('Pressione ENTER para recomeçar:')
    
# Lista dos valores
def um_nome():
    nomes = ['Marco', 'Carlos', 'Rodrigo', 'Maria', 'Roberta']
    return choice(nomes)

def um_email():
    emails = ['marco@gmail.com', 'carlosferreira@gmail.com', 'rodrigo@gmail.com', 'maria@gmail.com', 'roberta@gmail.com']
    return choice(emails)

def uma_cidade():
    cidades = ['Bom Jesus', 'Vacaria', 'Porto Alegre', 'Caxias do Sul', 'São José dos Ausentes']
    return choice(cidades)

def um_estado():
    estado = ['Rio Grande do Sul', 'Santa Catarina', 'Paraná', 'Mato Grosso', 'Rio de Janeiro']
    return choice(estado)

def um_telefone():
    telefones = ['(93) 96771-8731', '(87) 99963-0376', '(68) 99767-8766', '(73) 98161-9257', '(93) 96957-9871']
    return choice(telefones)

# Começando o programa
if __name__ == '__main__':
    entrada_de_valores()
