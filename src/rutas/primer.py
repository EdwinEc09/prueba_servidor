from db.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template

routes_primer = Blueprint("routes_primera", __name__)
from tablas.primera import primeras, primeraSchema

@routes_primer.route('/indexprimer', methods=['GET'] )
def indexinstitution():
    
    return render_template('/index.html')


@routes_primer.route('/guardarinstitution',methods=['POST'])
def saveinstitution():
    #request.form['title']

    #en el fullname va el dato de la db y en Roles de usuarios va la tbala donde se sacan los datos de la db
    nombre = request.form['nombre']
    apelldio = request.form['apelldio']
    print(nombre,nombre)
    new_primer = primeras(nombre)
    db.session.add(new_primer)
    db.session.commit()
    return nombre
    
