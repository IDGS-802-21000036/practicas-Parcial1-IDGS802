from wtforms import Form
from wtforms import StringField, IntegerField, RadioField

class PersonForm(Form):
    nombre = StringField("nombre")
    apaterno = StringField("apaterno")
    amaterno = StringField("amaterno")
    dia =  IntegerField("dia")
    mes = IntegerField("mes")
    anio = IntegerField("anio")
    sexo = RadioField("Sexo", choices=[("M", "Masculino"),("F", "Femenino")])

