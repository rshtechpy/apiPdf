import os
from flask import Flask, request, send_file
import pdfkit
import tempfile
from datetime import datetime

PDF_OUTPUT_DIR = os.environ.get("PDF_OUTPUT_DIR", "/pdfs")
WKHTMLTOPDF_PATH = os.environ.get("WKHTMLTOPDF_PATH", "/usr/bin/wkhtmltopdf")
FLASK_HOST = os.environ.get("FLASK_HOST", "0.0.0.0")
FLASK_PORT = int(os.environ.get("FLASK_PORT", 5001))

os.makedirs(PDF_OUTPUT_DIR, exist_ok=True)

app = Flask(__name__)


@app.route('/generar-pdf', methods=['POST'])
def generar_pdf():
    data = request.json
    html_content = data.get('plantilla', '')

    if not html_content:
        return {"error": "El campo 'plantilla' es requerido."}, 400

    try:
        # Crear un archivo PDF temporal usando pdfkit
        fecha_actual = datetime.now().strftime("%d%m%Y%H%M")
        nombre_archivo = f"presupuesto{fecha_actual}.pdf"
        pdf_path = os.path.join(PDF_OUTPUT_DIR, nombre_archivo)
        # Configuración de pdfkit para usar wkhtmltopdf
        config = pdfkit.configuration(wkhtmltopdf=WKHTMLTOPDF_PATH)
        # Opciones para wkhtmltopdf
        options = {
            'page-size': 'A4',  # Tamaño de la página
            'margin-top': '1mm',  # Márgenes reducidos
            'margin-right': '1mm',
            'margin-bottom': '1mm',
            'margin-left': '1mm',
            'encoding': 'UTF-8',  # Codificación
            'no-outline': None,  # Evitar contorno en el PDF
            'disable-smart-shrinking': None,  # Evitar que el contenido se reduzca automáticamente
            'dpi': 600,  # Aumentar la resolución
        }
        # Generar el PDF a partir del HTML recibido
        pdfkit.from_string(html_content, pdf_path, configuration=config, options=options)

        # Log informativo en consola
        print(f"[PDF generado] {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | IP: {request.remote_addr} | Archivo: {nombre_archivo}")
        # Devolver el archivo PDF generado con nombre dinámico
        return send_file(pdf_path, as_attachment=True, download_name=nombre_archivo, mimetype="application/pdf")
    
    except Exception as e:
        return {"error": str(e)}, 500

def mostrar_mensaje_inicio():
    url = f"http://{FLASK_HOST}:{FLASK_PORT}"
    print("\n" + "="*60, flush=True)
    print(f"\033[92mServicio corriendo en el puerto {FLASK_PORT}", flush=True)
    print(f"URL: {url}\033[0m", flush=True)
    print("-"*60, flush=True)
    print("\033[95mHecho con ❣️  por Skarious   github/skarious\033[0m", flush=True)
    print("="*60 + "\n", flush=True)

if __name__ == '__main__':
    mostrar_mensaje_inicio()
    app.run(host=FLASK_HOST, port=FLASK_PORT, debug=True)