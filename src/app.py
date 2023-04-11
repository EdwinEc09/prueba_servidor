#https://docs.sqlalchemy.org/en/14/core/type_basics.html
#https://flask.palletsprojects.com/en/2.2.x/
#from api.user import *
from flask import Flask,  redirect, request, jsonify, json, session, render_template
from config.db import db, app, ma



#importar los model en orden
from model.paciente import pacientes
from model.odontologo import odontologos

from model.cita import citas
from model.tratamiento import tratamientos
from model.histo_clinico import histoclinicos


'''
@app.route('/', methods=['GET'] )
def indexinstitution():
    
    return render_template('/index.html')
'''

@app.route('/index', methods=['GET'] )
def indexprimer():
    
    return "Hola Mundo!!"



#esto para que corra el server y ayuda con el puerto
if __name__ == '__main__':
   # load_dotenv()
    app.run(debug=True, port=5000, host='0.0.0.0')
    