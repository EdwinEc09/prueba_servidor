#https://docs.sqlalchemy.org/en/14/core/type_basics.html
#https://flask.palletsprojects.com/en/2.2.x/
#from api.user import *
from flask import Flask,  redirect, request, jsonify, json, session, render_template
from db.db import db, app, ma

from tablas.primera import primeras, primeraSchema

from rutas.primer import routes_primer

app.register_blueprint(routes_primer, url_prefix="/fronted")

#esto para que corra el server y ayuda con el puerto
if __name__ == '__main__':
   # load_dotenv()
    app.run(debug=True, port=5000, host='0.0.0.0')
    

primer_schema = primeraSchema()
primeras_schema = primeraSchema(many=True)

@app.route('/index', methods=['GET'] )
def indexprimer():
    
    return "Hola Mundo!!"
