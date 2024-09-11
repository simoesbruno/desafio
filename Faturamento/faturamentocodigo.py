import json


with open('faturamento.json', 'r') as file:
    dados = json.load(file)


faturamento = [dia["valor"] for dia in dados["faturamento_diario"] if dia["valor"] > 0]

menor_faturamento = min(faturamento)
maior_faturamento = max(faturamento)


media_mensal = sum(faturamento) / len(faturamento)

dias_acima_da_media = sum(1 for valor in faturamento if valor > media_mensal)

print(f"Menor valor de faturamento: {menor_faturamento}")
print(f"Maior valor de faturamento: {maior_faturamento}")
print(f"Dias com faturamento acima da média: {dias_acima_da_media}")
