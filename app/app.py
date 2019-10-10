import requests
from flask import Flask, render_template, request, Response
app = Flask(__name__)

class ESB():
    def __init__(self, Nombre):
        self.Nombre = Nombre


@app.route('/', methods=['GET','POST'])
def llamar_delete_complemento():
	Nombre = ""
	Correo = ""
	if request.method == 'POST':
		Nombre = request.form.get('nombre')
		Correo = request.form.get('correo')
		return 'Hola ' + Nombre
	return  '''<form method="POST">'''\
			'''Nombre: <input type="text" name="nombre"><br>'''\
			'''Correo: <input type="text" name="correo"><br>'''\
			'''<input type="submit" value="Submit"><br>'''\
			'''</form>'''

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')