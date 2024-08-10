from flask import Flask, render_template, request, redirect, url_for
from ahorcado import Ahorcado
from dotenv import load_dotenv

app = Flask(__name__)

# Crear una instancia del juego
juego = Ahorcado()

@app.route('/')
def elegir_dificultad():
        return render_template('dificultad.html')

@app.route('/iniciar/<nivel>')
def iniciar_juego(nivel):
        juego.iniciar(dificultad=nivel)
        return redirect(url_for('inicio'))

@app.route('/inicio')
def inicio():
        palabra = request.args.get('palabra')
        pista = request.args.get('pista')
        if palabra:
            juego.iniciar(palabra=palabra, pista=pista)
        return render_template(
            'template.html',
            palabra_a_mostrar=" ".join(juego.palabra_a_mostrar),
            pista=juego.obtener_pista(),
            intentos_restantes=juego.intentos_restantes,
            letras_usadas=juego.letras_usadas,
            juego_finalizado=juego.juego_finalizado,
            palabra_adivinada=juego.palabra_a_adivinar[0]
        )

@app.route('/intentar', methods=['POST'])
def intentar():
        letra = request.form['letra'].lower()
        if not juego.juego_finalizado:
            juego.intento(letra)
            juego.validar_fin_del_juego()
        return redirect(url_for('inicio'))

@app.route('/reiniciar')
def reiniciar():
    return redirect(url_for('elegir_dificultad'))
    

if __name__ == '__main__':
    app.run()
