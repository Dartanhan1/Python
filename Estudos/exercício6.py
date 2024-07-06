def maiores_que_media(conteudo: dict) -> list:
    # Calcular a média dos preços
    media = sum(conteudo.values()) / len(conteudo)
    
    # Filtrar os produtos cujo preço é superior à média
    produtos_acima_da_media = [(produto, preco) for produto, preco in conteudo.items() if preco > media]
    
    # Ordenar os produtos pelo preço (ordem crescente)
    produtos_acima_da_media = sorted(produtos_acima_da_media, key=lambda x: x[1])
    
    return produtos_acima_da_media

# Exemplo de uso
conteudo = {
    "arroz": 4.99,
    "feijão": 3.49,
    "macarrão": 2.99,
    "leite": 3.29,
    "pão": 1.99
}

print(maiores_que_media(conteudo))