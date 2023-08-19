from banco import *
from operacoes.deposito import depositar
from operacoes.consulta import consultarSaldo
from operacoes.saque import sacar
from operacoes.tranferencia import transferir

def menu():
    while True:
        print('---- SISTEMA BANCÁRIO ----')
        print('1 - Adicionar Conta')
        print('2 - Editar Conta')
        print('3 - Consultar conta')
        print('4 - Apagar conta')
        print('5 - Listar contas')
        print('6 - Atualizar nome')
        print('7 - Atualizar saldo')
        print('8 - Realizar saque')
        print('9 - Realizar deposito')
        print('10 - Consultar saldo')
        print('11 - Transferencia')
        print('12 - Sair')
        opcao = input('Selecione uma opção: ')

        