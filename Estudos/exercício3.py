from functools import reduce

def calcula_saldo(lancamentos) -> float:
    # Converter cada lançamento para seu valor apropriado (positivo para crédito e negativo para débito)
    valores = map(lambda x: x[0] if x[1] == 'C' else -x[0], lancamentos)
    
    # Usar reduce para somar todos os valores
    saldo_final = reduce(lambda acc, x: acc + x, valores)
    
    return saldo_final

# Exemplo de uso
lancamentos = [
    (200, 'D'),
    (300, 'C'),
    (100, 'C')
]

print(calcula_saldo(lancamentos))  # Deve imprimir 200
