# Use a imagem oficial do Python como base, antiga para ser mais leve
FROM python:3.9-slim

# Copie o arquivo canguru.py para dentro do container
COPY carguru.py /app/carguru.py

# Defina o diretório de trabalho como /app
WORKDIR /app

# Execute o código canguru.py quando o container for iniciado
CMD ["python", "carguru.py"]
