#de la libreria flask importamos Flask
from flask import Flask, render_template 
app = Flask(__name__) #designamos un objeto 'app'

@app.route("/") #creamos una ruta para la página principal
def home(): #definimos una funcion
    return render_template("home.html") #tomamoslo de un archivo html

@app.route('/about')
def about():
    return render_template('about.html') #tomamoslo de un archivo html

if __name__ == "__main__":
    app.run(debug=True) #Auto-reiniciar en cada cambio