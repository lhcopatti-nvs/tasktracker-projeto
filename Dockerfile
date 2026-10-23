# Imagem base leve com Python 3.11
FROM python:3.11-slim

# Pasta de trabalho dentro do container
WORKDIR /app

# Mostra as mensagens do Python na hora (sem buffer)
ENV PYTHONUNBUFFERED=1

# Copia o código da aplicação para dentro do container
COPY src/ /app/src/

# Comando que inicia o TaskTracker
CMD ["python", "src/main.py"]
