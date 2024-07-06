# Prática de Python com Containers Docker

## Objetivos
1. Criar um arquivo Dockerfile.
2. Utilizar comandos para execução do container.
3. Responder perguntas em formato Markdown.

Um arquivo chamado `canguru.py` está em uma pasta de destino `C:\Users\Estúdio\Documents\Repo DartanhanCompassUOL\Sprint 4\Desafio`.

## ETAPA 1: Construção e Execução do Container com `canguru.py`

### Dockerfile

```dockerfile
# Use a imagem oficial do Python como base
FROM python:3.9-slim

# Copie o arquivo canguru.py para dentro do container
COPY canguru.py /app/canguru.py

# Defina o diretório de trabalho como /app
WORKDIR /app

# Execute o código canguru.py quando o container for iniciado
CMD ["python", "canguru.py"]

# Construa a imagem a partir do Dockerfile
docker build -t carguru-image .

# Execute o container a partir da imagem criada
docker run carguru-image

```
## ETAPA 2: Reutilização de Containers
```
docker start nome_do_container
docker logs nome_do_container
```

## ETAPA 3: Container com Input Durante a Execução
```
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

# Use a imagem oficial do Python como base
FROM python:3.9-slim

# Crie o diretório de trabalho /app
WORKDIR /app

# Copie o script Python para dentro do container
COPY mascarar_dados.py .

# Execute o script Python quando o container for iniciado
CMD ["python", "mascarar_dados.py"]
# Construa a imagem a partir do Dockerfile
docker build -t mascarar-dados .

# Execute o container a partir da imagem criada, permitindo inputs durante a execução
docker run -it mascarar-dados
```
