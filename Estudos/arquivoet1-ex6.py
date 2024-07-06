import os

# Caminho para o arquivo CSV
csv_file = os.path.join(os.getcwd(), 'actors.csv')

# Etapa 1: Encontrar o ator com o maior número de filmes e sua quantidade correspondente.

max_movies_count = 0
max_movies_actor = ""

with open(csv_file, 'r') as file:
    # Pular cabeçalho
    file.readline()
    for line in file:
        # Dividir a linha usando a vírgula como separador
        data = line.strip().split(',')
        actor = data[0]
        num_movies = int(''.join(filter(str.isdigit, data[2])))  # Remover caracteres não numéricos
        if num_movies > max_movies_count:
            max_movies_count = num_movies
            max_movies_actor = actor

# Escrever o resultado no arquivo etapa1.txt
with open('etapa1.txt', 'w') as file:
    file.write(f"{max_movies_actor} - {max_movies_count} filmes\n")

# Etapa 2: Calcular a média de receita de bilheteria bruta dos principais filmes
total_gross_sum = 0
total_movies = 0

with open(csv_file, 'r') as file:
    # Pular cabeçalho
    file.readline()
    for line in file:
        # Dividir a linha usando a vírgula como separador
        data = line.strip().split(',')
        gross = float(data[5])  # Acessar a coluna correta para a receita bruta
        total_gross_sum += gross
        total_movies += 1

average_gross = total_gross_sum / total_movies

# Caminho para o arquivo de saída
output_file = "etapa2.txt"

# Escrever o resultado no arquivo etapa2.txt
with open(output_file, 'w') as file:
    file.write(f"Média de receita bruta dos principais filmes: ${average_gross:.2f} milhões\n")

