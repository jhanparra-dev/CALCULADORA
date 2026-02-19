from flask import Flask, request

app = Flask(__name__) #Inicializamos una aplicación Flask


@app.route('/') #Definimos la ruta raíz
def home(): #Definimos la función que se ejecutará cuando se acceda a la ruta raíz
    return '''

   <h1> Aplicación Calculadora </h1>

<ul> 

    <li><a href = "/suma"> suma  </a>  </li>
    <li> resta </li>
    <li> multiplicación </li>
    <li> división </li>

</ul>


'''
@app.route(sum) #Definimos la ruta para la suma
def ruta_suma():
    return f"La suma de los numeros a y b es: {a, b, a + b}" #Retornamos el resultado de la suma




    
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True) #Ejecutamos la aplicación en modo debug