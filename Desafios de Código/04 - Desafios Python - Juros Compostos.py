valor_inicial = float(input())
taxa_juros = float(input())
periodo = int(input())

valor_final = valor_inicial

for _ in range(periodo):
    valor_final *= (1 + taxa_juros)

print("Valor final do investimento: R$", round(valor_final, 2))
