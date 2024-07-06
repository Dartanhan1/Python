def etapa5():
    # Lista para armazenar tuplas de (nome do ator, receita bruta total)
    actors_gross = []

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
            # Verificando se a receita bruta total pode ser convertida em float
            try:
                total_gross = float(values[1])
                # Adicionando o ator e sua receita bruta à lista
                actors_gross.append((actor, total_gross))
            except ValueError:
                # Ignorando linhas com valores não numéricos na coluna Total Gross
                pass

    # Ordenando a lista de atores pela receita bruta em ordem decrescente
    sorted_actors = sorted(actors_gross, key=lambda x: (-x[1]))

    # Escrevendo o resultado no arquivo etapa5.txt
    with open('etapa5.txt', 'w') as output_file:
        for actor, gross in sorted_actors:
            output_file.write(f"{actor} - {gross}\n")

# Chamando a função etapa5 para executar
etapa5()

