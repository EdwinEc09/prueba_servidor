from flask import Blueprint, request, jsonify, json
from db.db import db, app, ma
from flask import Flask,  redirect, request, jsonify, json, session, render_template

from tablas.primera import  primeras,primeraSchema

routes_primeraa = Blueprint("routes_institucion", __name__)

#libros

InstitucionSchema = primeraSchema()
institucionesSchema = primeraSchema(many=True)


@routes_primeraa.route('/primerr', methods=['GET'])
def libros():    
    returnall = primeras.query.all()
    resultado_institucion = primeras.dump(returnall)
    return jsonify(resultado_institucion)
