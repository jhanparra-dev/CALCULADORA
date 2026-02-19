from flask import Flask, request

from random import randint

app = Flask (__name__)

@app.route("/")
def home():
    return '''

<h1> Aplicación Calculadora </h1>

<p> Opciones disponibles </p>

<ul>

    <li><a href="suma?a=8&b=12"> 
    Suma </a></li>
    <li><a href="resta?a=8&b=12"> 
    Resta  </a></li>
    <li><a href="multiplicacion?a=8&b=12"> 
    Multiplicación </a></li>
    <li><a href="division?a=8&b=12"> 
    División </a></li>
    <li><a href="random"> 
    Número aleatorio </a></li>




</ul>

'''

#esta es una ruta adicional en la aplicación

@app.route("/suma", methods=["GET"])
def ruta_suma():
    a = request.args.get("a", type=float)
    b = request.args.get("b", type=float)
    resultado=a+b
    return f"La suma de los números {a} y {b} es: {resultado}, pulsa para volver <a href='/'>Home</a> "

@app.route("/resta")
def ruta_resta():
    a = request.args.get("a", type=float)
    b = request.args.get("b", type=float)
    resultado=a-b
    return f"La resta de los números {a} y {b} es: {resultado}, pulsa para volver <a href='/'>Home</a> "

@app.route("/multiplicacion")
def ruta_multiplicacion():
    a = request.args.get("a", type=float)
    b = request.args.get("b", type=float)
    resultado=a*b
    return f"La multiplicación de los números {a} y {b} es: {resultado},pulsa para volver <a href='/'>Home</a> "

@app.route("/division")
def ruta_division():
    a = request.args.get("a", type=float)
    b = request.args.get("b", type=float)
    resultado=a//b
    return f"La división de los números {a} y {b} es: {resultado}, pulsa para volver <a href='/'>Home</a>"

@app.route("/random")
def ruta_random():
    import random
    resultado=random.randint(1,100)
    return f"El número aleatorio generado es: {resultado}, pulsa para volver <a href='/'>Home</a>"    

# Punto de entrada
if __name__ == "__main__":
    # Ejecuta el servidor de desarrollo en localhost:5000
    app.run(host="0.0.0.0", port=5000, debug=True)
