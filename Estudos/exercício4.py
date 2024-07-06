def calcular_valor_maximo(operadores, operandos) -> float:
    # Função para aplicar a operação entre dois operandos
    def aplicar_operacao(op, a, b):
        if op == '+':
            return a + b
        elif op == '-':
            return a - b
        elif op == '*':
            return a * b
        elif op == '/':
            return a / b
        elif op == '%':
            return a % b
        else:
            raise ValueError(f"Operador desconhecido: {op}")
    
    # Combinar operadores e operandos
    combinados = zip(operadores, operandos)
    
    # Aplicar as operações usando map
    resultados = map(lambda x: aplicar_operacao(x[0], x[1][0], x[1][1]), combinados)
    
    # Encontrar o valor máximo
    valor_maximo = max(resultados)
    
    return valor_maximo

# Exemplo de uso
operadores = ['+','-','*','/','+']
operandos  = [(3, 6), (-7, 4.9), (8, -8), (10, 2), (8, 4)]

print(calcular_valor_maximo(operadores, operandos))  # Deve imprimir 12