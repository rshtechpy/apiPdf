# 📝 API PDF Generator 🚀

¡Convierte HTML a PDF fácilmente usando una API REST en Docker!
Hecho con ❣️ por [Skarious](https://github.com/skarious)

---

## 📦 Despliegue rápido con Docker Compose

1. **Clona este repositorio**  
   ```bash
   git clone https://github.com/skarious/tu-repo.git
   cd tu-repo/docker
   ```

2. **Configura el stack**  
   Las variables de entorno ya están incluidas en el `docker-compose.yml`.  
   Si quieres cambiar el puerto, solo edítalo ahí.

3. **Levanta el servicio**  
   ```bash
   docker-compose up -d
   ```

4. **¡Listo!**  
   Accede a la API en:  
   `http://localhost:5001/generar-pdf`

---

## 🛠️ Endpoints

### POST `/generar-pdf`

Convierte HTML a PDF y descarga el archivo generado.

#### Ejemplo de petición (curl/Postman):

```bash
curl --location --request POST 'http://localhost:5001/generar-pdf' \
--header 'Content-Type: application/json' \
--data-raw '{
  "plantilla": "<h1>Hola PDF desde Postman!</h1>"
}'
```

#### Respuesta
- Descarga directa del archivo PDF generado.

---

## ⚙️ Variables de entorno

Estas variables están en el `docker-compose.yml`:

| Variable            | Descripción                           | Valor por defecto           |
|---------------------|---------------------------------------|-----------------------------|
| FLASK_HOST          | Host donde corre Flask                | 0.0.0.0                     |
| FLASK_PORT          | Puerto de la API                      | 5001                        |
| WKHTMLTOPDF_PATH    | Ruta de wkhtmltopdf en el contenedor  | /usr/bin/wkhtmltopdf        |
| PYTHONUNBUFFERED    | Logs en tiempo real                   | 1                           |

---

## 🗂️ Volúmenes

- Los archivos PDF generados se guardan en la carpeta `./pdfs` de tu máquina.

---

## 🐳 Publicación en Docker Hub

Imagen disponible en:  
`skarious/apipdf:latest`

---

## ❤️ Créditos

Hecho con ❣️ por Skarious  
[github.com/skarious](https://github.com/skarious)

---

## 📋 Licencia

MIT
