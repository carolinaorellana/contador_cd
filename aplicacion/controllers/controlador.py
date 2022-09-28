from aplicacion import app
from flask import Flask, render_template, request, redirect, session

@app.route('/')
def contador():
    if 'visitas' in session:
        session['visitas']+= 1 #si hay visitas en la sesion suma 1
    else:
        session['visitas'] = 1 #sino hay visitas crea las visitas =1
        session['contador']= 0
    return render_template('index.html')

@app.route('/destruir_sesion', methods=['POST'])#Agrega una ruta "/destroy_session" que elimine la sesión y redirija a la ruta raíz. Pruébalo.
def destruir_sesion():
    session.clear()
    return redirect('/')

@app.route('/agregar_dos', methods=['POST']) #agrega un botón +2 debajo del contador y una nueva ruta que incremente el contador en 2
def agregar_dos():
    session['contador']+= 2
    return redirect('/')

@app.route('/sumar', methods=['POST']) #agrega un botón +2 debajo del contador y una nueva ruta que incremente el contador en 2
def sumar():
    sum = int(request.form["sumar"]) 
    session['contador']+= sum
    return redirect('/')

#BONUS SENSEI: ajusta tu código para mostrar el número de veces que el usuario ha visitado la página y el valor del contador, dada la funcionalidad anterior

