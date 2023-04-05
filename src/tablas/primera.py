from db.db import db, app, ma 

class primeras(db.Model):
    __tablename__ = "tblprimera"

    
    id  = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    apellido = db.Column(db.String(50))

    def __init__(self, primer):
        self.primer = primer
    
with app.app_context():
    db.create_all()

class primeraSchema(ma.Schema):
    class Meta:
        fields = ('id','nombre','apellido')
