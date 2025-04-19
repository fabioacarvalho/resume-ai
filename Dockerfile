# Usa a imagem oficial do Python 3.12
FROM python:3.12

# Define o diretório de trabalho
WORKDIR /app

# Evita que o Python crie arquivos .pyc
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Instala dependências do sistema necessárias para compilar dlib e outros pacotes
RUN apt-get update && apt-get install -y \
    cmake \
    libsm6 \
    libxext6 \
    libxrender-dev \
    build-essential \
    python3-dev \
    libgl1-mesa-glx \
    && rm -rf /var/lib/apt/lists/*

# Copia os arquivos do projeto para o container
COPY requirements.txt /app/

# Instala as dependências do Python
RUN pip install --no-cache-dir --upgrade pip \
&& pip install --no-cache-dir -r requirements.txt

COPY . /app/

# Expõe a porta 8080
EXPOSE 8080

# Comando para rodar o Streamlit
CMD ["streamlit", "run", "./Home.py", "--server.port", "8080", "--server.address", "0.0.0.0"]