from wtforms import Form
from wtforms import StringField,IntegerField, EmailField, validators, SelectField, RadioField

class DistanceForm(Form):
    x1 = IntegerField("x1")
    x2 = IntegerField("x2")
    
    y1 = IntegerField("y1")
    y2 = IntegerField("y2")

class DictionaryForm(Form):
    ingles = StringField("ingles",[validators.DataRequired(message='el campo es requerido'), validators.length(min=3,max=10,message='ingresa palabra valida')])
    espaniol = StringField("espaniol",[validators.DataRequired(message='el campo es requerido'), validators.length(min=3,max=10,message='ingresa palabra valida')])

class ConsultaDiccionarioForm(Form):
    palabra = StringField("palabra",[validators.DataRequired(message='el campo es requerido'), validators.length(min=3,max=10,message='ingresa palabra valida')])
    rdConsulta = RadioField('rdConsulta', choices=[("Ingles","Ingles"), ("Espaniol","Español")])
    
class PersonForm(Form):
    nombre = StringField("nombre")
    apaterno = StringField("apaterno")
    amaterno = StringField("amaterno")
    dia =  IntegerField("dia")
    mes = IntegerField("mes")
    anio = IntegerField("anio")
    sexo = RadioField("Sexo", choices=[("M", "Masculino"),("F", "Femenino")])