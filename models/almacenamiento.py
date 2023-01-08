from odoo import _, api, fields, models

class Almacenamiento(models.Model):
    _name = "almacenamiento"
    _rec_name = "nombre"
    _description = "portatiles"

    marca = fields.Char(string="Marca", required=True )
    modelo = fields.Char(string="Modelo" , required=True)
    caracteristicas = fields.Text(string="Caracteristicas")
    espacio = fields.Selection([('500gb','500GB'),('1tb','1TB'),('2tb','2TB')])
    imagen = fields.Binary(string="Imagen")
    rpm = fields.Integer(string="RPM")
    if(tipo=='ssd'):
        velocidad_lectura = fields.Integer(string="Velocidad de lectura")
        velocidad_escritura = fields.Integer(string="Velocidad de escritura")