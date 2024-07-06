def etapa2():
    # Leitura do arquivo actors.csv
    with open('actors.csv', 'r') as file:
        # Ignorando o cabeçalho
        next(file)
        total_gross_sum = 0
        movie_count = 0
        # Iterando sobre cada linha do arquivo
        for line in file:
            # Separando os valores pelo caractere ','
            values = line.strip().split(',')
            # Tentando converter o valor da receita bruta para float
            try:
                gross = float(values[5])
                # Somando a receita bruta de cada filme
                total_gross_sum += gross
                # Contando o número de filmes
                movie_count += 1
            except ValueError:
                # Ignorando valores que não podem ser convertidos para float
                pass

    # Verificando se não houve filmes no conjunto de dados
    if movie_count == 0:
        average_gross = 0
    else:
        # Calculando a média da receita bruta
        average_gross = total_gross_sum / movie_count

    # Escrevendo o resultado no arquivo etapa2.txt
    with open('etapa2.txt', 'w') as output_file:
        output_file.write(f"{average_gross}")

# Chamando a função etapa2 para executar
etapa2()



