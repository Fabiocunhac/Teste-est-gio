
faturamento_por_estado = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

valor_total = sum(faturamento_por_estado.values())

percentuais = {estado: (valor / valor_total) * 100 for estado, valor in faturamento_por_estado.items()}

print("Percentual de representação de cada estado no faturamento mensal:")
for estado, percentual in percentuais.items():
    print(f"{estado}: {percentual:.2f}%")
