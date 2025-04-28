FROM python:3.11-slim

# Instalar dependencias del sistema y wkhtmltopdf
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        wkhtmltopdf \
        build-essential \
        libssl-dev \
        libffi-dev \
        libxrender1 \
        libxext6 \
        libfontconfig1 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Crear carpeta para PDFs
RUN mkdir /pdfs

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar requirements e instalar dependencias de Python
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código fuente
COPY . .

# Variable de entorno por defecto para wkhtmltopdf
ENV WKHTMLTOPDF_PATH=/usr/bin/wkhtmltopdf
ENV FLASK_HOST=0.0.0.0
ENV FLASK_PORT=5001

# Exponer el puerto
EXPOSE 5001

# Comando para ejecutar la app con gunicorn
CMD ["gunicorn", "-w", "2", "-b", "0.0.0.0:5001", "-c", "gunicorn_conf.py", "pdf:app"]
