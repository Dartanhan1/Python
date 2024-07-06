import csv

def processar_notas(nome_arquivo):
    with open(nome_arquivo, 'r') as file:
        reader = csv.reader(file)
        estudantes = [row for row in reader]
    
    # Função para processar cada linha de dados do estudante
    def processar_estudante(estudante):
        nome = estudante[0]
        notas = list(map(float, estudante[1:]))
        tres_maiores_notas = sorted(notas, reverse=True)[:3]
        media_tres_maiores = round(sum(tres_maiores_notas) / 3, 2)
        return nome, tres_maiores_notas, media_tres_maiores
    
    # Processar todos os estudantes
    resultados = list(map(processar_estudante, estudantes))
    
    # Ordenar os resultados pelo nome do estudante
    resultados_ordenados = sorted(resultados, key=lambda x: x[0])
    
    # Imprimir os resultados
    for nome, notas, media in resultados_ordenados:
        notas_formatadas = [int(nota) for nota in notas]  # Ajuste aqui
        print(f"Nome: {nome} Notas: {notas_formatadas} Média: {media}")

# Exemplo de uso
processar_notas('estudantes.csv')
