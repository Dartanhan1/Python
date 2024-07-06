# Use a imagem oficial do Python como base, antiga para ser mais leve
FROM python:3.9-slim

# Crie o diretório de trabalho /app
WORKDIR /app

# Copie o script Python para dentro do container
COPY mascarar_dados.py .

# Execute o script Python quando o container for iniciado
CMD ["python", "mascarar_dados.py"]
