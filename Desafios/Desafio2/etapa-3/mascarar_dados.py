import hashlib

def main():
    while True:
        # Recebe uma string via input
        texto = input("Digite a string a ser mascarada (ou 'exit' para sair): ")

        if texto.lower() == 'exit':
            break

        # Gera o hash SHA-1 da string
        hash_texto = hashlib.sha1(texto.encode()).hexdigest()

        # Imprime o hash
        print("Hash SHA-1 da string:", hash_texto)

if __name__ == "__main__":
    main()

