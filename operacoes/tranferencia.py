from banco import obterConta, banco


def transferir(contaOri: int, contaDes: int, valor: float) -> None:
    contaOrigem = obterConta(contaOri)
    contaDestino = obterConta(contaDes)
    if contaOrigem and contaDestino:
        if contaOrigem['saldo'] >= valor:
            contaDestino['saldo'] += valor
            contaOrigem['saldo'] -= valor
            print('Transferencia realizada com sucesso!')
        else:
            print('Saldo insulficiente para transferencia!')
    else:
        print('Uma das contas não existe!')
