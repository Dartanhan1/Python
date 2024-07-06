with open('number.txt', 'r') as file:
    numeros = file.readlines()

numeros = list(map(int, numeros))

numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))

numeros_pares_ordenados = sorted(numeros_pares, reverse=True)

maiores_pares = numeros_pares_ordenados[:5]

soma_maiores_pares = sum(maiores_pares)

print(maiores_pares)
print(soma_maiores_pares)
