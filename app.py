from flask import Flask, request, render_template
import qrcode
from io import BytesIO
import base64
from PIL import Image, ImageTk
import json


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generar_qr', methods=['POST'])
def generar_qr():
    data = request.form['data']
    data1 = request.form["data1"]
    data2 = request.form["data2"]
    data3 = request.form["data3"]
    data4 = request.form["data4"]
    data5 = request.form["data5"]
    data6 = request.form["data6"]

    data7 = f"nombre: {data} {data1} {data2}\nNumero de control: {data3}\nTipo de sangre: {data4}\nNSS{data5}\nNumero de contacto{data6}"
    dicc={"nombre":data, "apellido paterno":data1, "apellido materno: ":data2, "Numero de control: ":data3, "Tipo de sangre: ":data4, "NSS:":data5, "Numero de contacto: ":data6}
    
    # Configuración del QR
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data7)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    
    # Convertir la imagen a un string base64
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    img_str = base64.b64encode(buffer.getvalue()).decode("utf-8")
    
    return render_template('resultados.html', qr_data=img_str, data=dicc)

if __name__ == '__main__':
    app.run(debug=True)
