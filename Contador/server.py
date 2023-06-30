from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "esto es secreto"

@app.route('/')
def agregar_contador():
    if 'contador' not in session:
        session['contador'] = 0
    return render_template('index.html', contador=session['contador'])


@app.route('/visitas')
def agregar_visitas():
    if 'visitas' not in session:
        session['visitas'] = 0
    else:
        session['visitas'] += 1
    return render_template('index.html', visitas=session['visitas'])

@app.route('/contador', methods=['POST'])
def agregar_dos_contador():
    if 'contador' in session:
        session ['contador'] += 2
    return redirect('/')

@app.route('/destroy_session')
def eliminar_session():
    session.clear()
    return redirect ("/")

@app.route('/resetear', methods=['POST'])
def resetear_contador():
    session['contador']=0
    session['visitas']=0
    return redirect('/')

@app.route('/incrementar', methods=['POST'])
def incrementar_contador():
    incrementar = int(request.form['incrementar'])
    session ['contador'] += incrementar
    return redirect('/')


if __name__=="__main__":
    app.run(debug=True)