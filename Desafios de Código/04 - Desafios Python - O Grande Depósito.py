valor = float(input())

if valor > 0:
    saldo_atual = valor
    print("Deposito realizado com sucesso!")
    print(f"Saldo atual: R$ {saldo_atual:.2f}")
elif valor < 0:
    print("Valor invalido! Digite um valor maior que zero.")
else:
    print("Encerrando o programa...")
