def conta_vogais(texto: str) -> int:
    # Definindo as vogais que queremos contar
    vogais = 'aeiouAEIOU'
    
    # Usando filter para manter apenas as vogais
    apenas_vogais = filter(lambda char: char in vogais, texto)
    
    # Contando o número de vogais usando len
    return len(list(apenas_vogais))

# Exemplo de uso
texto = "Exemplo de string para contagem de vogais"
print(conta_vogais(texto))  # Deve imprimir o número de vogais na string