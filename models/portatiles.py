from odoo import _, api, fields, models

class Portatiles(models.Model):
    _name = "portatiles"
    _rec_name = "nombre"
    _description = "portatiles"
    
    nombre = fields.Char(string="Nombre", requiered=True)
    marca = fields.Char(string="Marca", requiered=True )
    CPU = fields.Char(string="CPU")
    tipo = fields.Char(string="tipo")
    fecha_compra = fields.Date(string="Fecha de compra")
    tiempo_uso = fields.Integer(string="Tiempo de uso", required=True)
    caracteristicas = fields.Text(string="Caracteristicas")
    precio = fields.Float(string="Precio", requiered=True)
    imagen = fields.Binary(string="Imagen")
    vendedor = fields.Many2one('usuarios', required=True)
    vendido = fields.Boolean(string="Vendido", compute='_vendido')
    RAM= fields.Char(string="RAM")

    @api.depends('vendedor')
    def _vendido(self):
        for record in self:
            for venta in record.vendedor.ventas:
                if venta.portatil == self:
                    record.vendido = True
                else:
                    record.vendido = False
    
    @api.depends('vendedor')
    def _vendido(self):
        for record in self:
            for venta in record.vendedor.ventas:
                # si se ha vendido que se elimine de la lista de portatiles
                if venta.portatil == self:
                    record.vendido = True
                    self.unlink()
                else:
                    record.vendido = False
