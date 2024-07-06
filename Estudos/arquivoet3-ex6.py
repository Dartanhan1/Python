def etapa3():
    # Variáveis para armazenar o nome do ator com a maior média e a própria maior média
    max_average_actor = ''
    max_average_gross_per_movie = 0

    # Leitura do arquivo actors.csv
    with open('actors.csv', 'r') as file:
        # Ignorando o cabeçalho
        next(file)
        # Iterando sobre cada linha do arquivo
        for line in file:
            # Separando os valores pelo caractere ','
            values = line.strip().split(',')
            # Obtendo o nome do ator
            actor = values[0]
            # Obtendo a média de receita bruta por filme
            average_gross_per_movie = float(values[3])
            # Verificando se a média atual é maior que a máxima anterior
            if average_gross_per_movie > max_average_gross_per_movie:
                max_average_gross_per_movie = average_gross_per_movie
                max_average_actor = actor

    # Escrevendo o resultado no arquivo etapa3.txt
    with open('etapa3.txt', 'w') as output_file:
        output_file.write(f"{max_average_actor} - {max_average_gross_per_movie}")

# Chamando a função etapa3 para executar
etapa3()
