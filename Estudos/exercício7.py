def pares_ate(n: int):
    for num in range(2, n + 1, 2):
        yield num

# Exemplo de uso
for par in pares_ate(10):
    print(par)