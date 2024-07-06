def etapa4():
    # Dicionário para armazenar a contagem de cada filme
    movie_counts = {}

    # Leitura do arquivo actors.csv
    with open('actors.csv', 'r') as file:
        # Ignorando o cabeçalho
        next(file)
        # Iterando sobre cada linha do arquivo
        for line in file:
            # Separando os valores pelo caractere ','
            values = line.strip().split(',')
            # Obtendo o nome do filme de maior bilheteria
            movie = values[4]
            # Incrementando a contagem do filme no dicionário
            movie_counts[movie] = movie_counts.get(movie, 0) + 1

    # Ordenando os filmes por contagem decrescente e, em segundo nível, pelo nome do filme
    sorted_movies = sorted(movie_counts.items(), key=lambda x: (-x[1], x[0]))

    # Escrevendo o resultado no arquivo etapa4.txt
    with open('etapa4.txt', 'w') as output_file:
        for movie, count in sorted_movies:
            output_file.write(f"{movie} - {count}\n")

# Chamando a função etapa4 para executar
etapa4()
