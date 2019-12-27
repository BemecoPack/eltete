
from odoo import fields, models, api



class ProductTemplate(models.Model):
    _inherit = 'product.template'
    
    und_pallet = fields.Integer('Unidades pallet', readonly=True)
    attribute_id = fields.Many2one('sale.product.attribute', string="Atributo producto", readonly=True, )
    referencia_cliente_id = fields.Many2one('sale.referencia.cliente', string='Referencia cliente', store=True, related='attribute_id.referencia_cliente_id')
    referencia_id = fields.Many2one('product.referencia', string='Referencia', store=True, related='attribute_id.referencia_cliente_id.referencia_id')

	

###############################
# CARACTERISTICAS REF CLIENTE #
###############################    

class ProductCaracteristicaPalletEspecial(models.Model):
    _name = 'product.caracteristica.pallet.especial'
    _order = 'number'
    
    name = fields.Char('Nombre', required=True)
    number = fields.Integer('Número', required=True)
    active = fields.Boolean('Activo', default=True)
    description = fields.Char('Descripción')
    incremento = fields.Float('Incremento', digits=(8, 4), required = True)
    
    TIPO_SEL = [('1', 'Metro de Producto'), 
               ('2', 'Unidad de Producto'),
               ('3', 'Porcentaje de Producto'),                 
               ('4', 'Por Pallet'),
               ]
    tipo = fields.Selection(selection = TIPO_SEL, string = 'Tipo')
    


############################
# CARACTERISTICAS ATRIBUTO #
############################  

## CANTONERA ##



class ProductCaracteristicaCantoneraColor(models.Model):
    _name = 'product.caracteristica.cantonera.color'
    _order = 'number'
    
    name = fields.Char('Nombre', required=True)
    number = fields.Integer('Número', required=True)
    description = fields.Char('Descripción')
    
    active = fields.Boolean('Activo', default = True)
    valido = fields.Boolean('Valido para Fabricar', default = False)

    incremento = fields.Float('Incremento', digits=(8, 4), default = 0, required = True)
    TIPO_SEL = [('1', 'Metro de Producto'),   
                ('2', 'Unidad de Producto'),
                ('3', 'Porcentaje de Producto'),
                ('4', 'Por Pallet'),
                ]
    tipo = fields.Selection(selection = TIPO_SEL, string = 'Tipo', required = True)
    
    
    
class ProductCaracteristicaCantoneraForma(models.Model):
    _name = 'product.caracteristica.cantonera.forma'
    _order = 'number'
    
    name = fields.Char('Nombre', required=True)
    number = fields.Integer('Número', required=True)
    description = fields.Char('Descripción')
    active = fields.Boolean('Activo', default = True)
    incremento = fields.Float('Incremento', digits=(8, 4), default = 0, required = True)
    TIPO_SEL = [('1', 'Metro de Producto'),   
                ('2', 'Unidad de Producto'),
                ('3','Porcentaje de Producto'),
                ('4', 'Por Pallet'),
                ]
    tipo = fields.Selection(selection = TIPO_SEL, string = 'Tipo', required = True)
    cantonera_1 = fields.Boolean('Cantonera 1', default = False)
    cantonera_2 = fields.Boolean('Cantonera 2', default = False)
    cantonera_3 = fields.Boolean('Cantonera 3', default = False)
    cantonera_4 = fields.Boolean('Cantonera 4', default = False)



class ProductCaracteristicaCantoneraEspecial(models.Model):
    _name = 'product.caracteristica.cantonera.especial'
    _order = 'number'
    
    name = fields.Char('Nombre', required=True)
    number = fields.Integer('Número', required=True)
    description = fields.Char('Descripción')
    active = fields.Boolean('Activo', default = True)
    incremento = fields.Float('Incremento', digits=(8, 4), required = True)
    TIPO_SEL = [('1', 'Metro de Producto'),   
                ('2', 'Unidad de Producto'),
                ('3', 'Porcentaje de Producto'),
                ('4', 'Por Pallet'),
                ]
    tipo = fields.Selection(selection = TIPO_SEL, string = 'Tipo', required = True)
    cantonera_1 = fields.Boolean('Cantonera 1', default = False)
    cantonera_2 = fields.Boolean('Cantonera 2', default = False)
    cantonera_3 = fields.Boolean('Cantonera 3', default = False)
    cantonera_4 = fields.Boolean('Cantonera 4', default = False)



class ProductCaracteristicaCantoneraImpresion(models.Model):
    _name = 'product.caracteristica.cantonera.impresion'
    _order = 'number'
    
    name = fields.Char('Nombre', required=True)
    number = fields.Integer('Número', required=True)
    description = fields.Char('Descripción')
    active = fields.Boolean('Activo', default = True)
    num_tintas = fields.Integer('Numero de Tintas')
    incremento = fields.Float('Incremento', digits=(8, 4), required = True)
    TIPO_SEL = [('1', 'Metro de Producto'),   
                ('2', 'Unidad de Producto'),
                ('3', 'Porcentaje de Producto'),
                ('4', 'Por Pallet'),
                ]
    tipo = fields.Selection(selection = TIPO_SEL, string = 'Tipo', required = True)
    cantonera_1 = fields.Boolean('Cantonera 1', default = False)
    cantonera_2 = fields.Boolean('Cantonera 2', default = False)
    cantonera_3 = fields.Boolean('Cantonera 3', default = False)
    cantonera_4 = fields.Boolean('Cantonera 4', default = False)


## PERFILU ##


class ProductCaracteristicaPerfiluColor(models.Model):
    _name = 'product.caracteristica.perfilu.color'
    _order = 'number'
    
    name = fields.Char('Nombre', required=True)
    number = fields.Integer('Número', required=True)
    description = fields.Char('Descripción')
    
    active = fields.Boolean('Activo', default = True)
    valido = fields.Boolean('Valido para Fabricar', default = False)
    incremento = fields.Float('Incremento', digits=(8, 4), default = 0, required = True)
    TIPO_SEL = [('1', 'Metro de Producto'),   
                ('2', 'Unidad de Producto'),
                ('3', 'Porcentaje de Producto'),
                ('4', 'Por Pallet'),
                ]
    tipo = fields.Selection(selection = TIPO_SEL, string = 'Tipo', required = True)
    


## TODOS ##        
    
class ProductCaracteristicaReciclable(models.Model):
    _name = 'product.caracteristica.reciclable'
    _order = 'number'
    
    name = fields.Char('Nombre', required=True)
    number = fields.Integer('Número', required=True)
    description = fields.Char('Descripción')
    active = fields.Boolean('Activo', default = True)
    incremento = fields.Float('Incremento', digits=(8, 4), required = True)
    TIPO_SEL = [('1', 'Metro de Producto'),   
                ('2', 'Unidad de Producto'),
                ('3', 'Porcentaje de Producto'),
                ('4', 'Por Pallet'),
                ]
    tipo = fields.Selection(selection = TIPO_SEL, string = 'Tipo', required = True)
    cantonera_1 = fields.Boolean('Cantonera 1', default = False)
    cantonera_2 = fields.Boolean('Cantonera 2', default = False)
    cantonera_3 = fields.Boolean('Cantonera 3', default = False)
    cantonera_4 = fields.Boolean('Cantonera 4', default = False)
    
    
class ProductCaracteristicaFSC(models.Model):
    _name = 'product.caracteristica.fsc'
    _order = 'number'
    
    name = fields.Char('Nombre', required=True)
    number = fields.Integer('Número', required=True)
    description = fields.Char('Descripción')
    active = fields.Boolean('Activo', default = True)
    incremento = fields.Float('Incremento', digits=(8, 4), required = True)
    TIPO_SEL = [('1', 'Metro de Producto'),   
                ('2', 'Unidad de Producto'),
                ('3', 'Porcentaje de Producto'),
                ('4', 'Por Pallet'),
                ]
    tipo = fields.Selection(selection = TIPO_SEL, string = 'Tipo', required = True)
    cantonera_1 = fields.Boolean('Cantonera 1', default = False)
    cantonera_2 = fields.Boolean('Cantonera 2', default = False)
    cantonera_3 = fields.Boolean('Cantonera 3', default = False)
    cantonera_4 = fields.Boolean('Cantonera 4', default = False)
    

class ProductCaracteristicaInglete(models.Model):
    _name = 'product.caracteristica.inglete'
    _order = 'number'
    
    name = fields.Char('Nombre', required=True)
    number = fields.Integer('Número', required=True)
    description = fields.Char('Descripción')
    active = fields.Boolean('Activo', default = True)
    
    incremento = fields.Float('Incremento', digits=(8, 4), default = 0, required = True)
    TIPO_SEL = [('1', 'Metro de Producto'),   
                ('2', 'Unidad de Producto'),
                ('3', 'Porcentaje de Producto'),
                ('4', 'Por Pallet'),
                ]
    tipo = fields.Selection(selection = TIPO_SEL, string = 'Tipo', required = True)



class ProductCaracteristicaPlanchacolor(models.Model):
    _name = 'product.caracteristica.planchacolor'
    _order = 'number'
    
    name = fields.Char('Nombre', required=True)
    number = fields.Integer('Número', required=True)
    description = fields.Char('Descripción')
    active = fields.Boolean('Activo', default = True)
    
    valido = fields.Boolean('Valido para Fabricar', default = False)
    incremento = fields.Float('Incremento', digits=(8, 4), required = True)
    TIPO_SEL = [('1', 'Metro Cuadrado de Producto'),   
                ('2', 'Unidad de Producto'),
                ('3', 'Porcentaje de Producto'),
                ('4', 'Por Pallet'),
                ]
    tipo = fields.Selection(selection = TIPO_SEL, string = 'Tipo', required = True)




    
    
class ProductCaracteristicaTroquelado(models.Model):
    _name = 'product.caracteristica.troquelado'
    _order = 'number'
    
    name = fields.Char('Nombre', required=True)
    number = fields.Integer('Número', required=True)
    description = fields.Char('Descripción')
    active = fields.Boolean('Activo', default = True)
    incremento = fields.Float('Incremento', digits=(8, 4), required = True)
    TIPO_SEL = [('1', 'Metro Cuadrado de Producto'),   
                ('2', 'Unidad de Producto'),
                ('3', 'Porcentaje de Producto'),
                ('4', 'Por Pallet'),
                ]
    tipo = fields.Selection(selection = TIPO_SEL, string = 'Tipo', required = True)
    troqueladora_1 = fields.Boolean('Troqueladora 1', default = False)
    troqueladora_2 = fields.Boolean('Troqueladora 2', default = False)
    
    
class ProductCaracteristicaPapelCalidad(models.Model):
    _name = 'product.caracteristica.papelcalidad'
    _order = 'number'
    
    name = fields.Char('Nombre', required=True)
    number = fields.Integer('Número', required=True)
    description = fields.Char('Descripción')
    active = fields.Boolean('Activo', default = True)
    incremento = fields.Float('Incremento', digits=(8, 4), required = True)
    TIPO_SEL = [('1', 'Metro Cuadrado de Producto'),   
                ('2', 'Unidad de Producto'),
                ('3', 'Porcentaje de Producto'),
                ('4', 'Por Pallet'),
                ]
    tipo = fields.Selection(selection = TIPO_SEL, string = 'Tipo', required = True)
