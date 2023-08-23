saldo_atual = float(input())
valor_deposito = float(input())
valor_retirada = float(input())

saldo_atualizado = saldo_atual + valor_deposito - valor_retirada

print(f"Saldo atualizado na conta: {saldo_atualizado:.1f}")
