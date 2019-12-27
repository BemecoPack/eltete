from odoo import fields, models, api


class ProductReferencia(models.Model):
    _name = 'product.referencia'

    type_id = fields.Many2one('product.category', string="Tipo de producto", required=True)
  
    is_cantonera = fields.Boolean('¿Es Cantonera?', related='type_id.is_cantonera')
    is_perfilu = fields.Boolean('¿Es Perfil U?', related='type_id.is_perfilu')
    is_slipsheet = fields.Boolean('¿Es Slip Sheet?', related='type_id.is_slipsheet')
    is_solidboard = fields.Boolean('¿Es Solid Board?', related='type_id.is_solidboard')
    is_formato = fields.Boolean('¿Es Formato?', related='type_id.is_formato')
    is_bobina = fields.Boolean('¿Es Bobina?', related='type_id.is_bobina')
    is_pieballet = fields.Boolean('¿Es Pie de Ballet?', related='type_id.is_pieballet')
    is_varios = fields.Boolean('¿Es Varios?', related='type_id.is_varios')
    
    name = fields.Char('Nombre', readonly=True)
    TIPO_PIE = [('1', 'Alto 100'), 
               ('2', 'Alto 60'),
               ]
    pie = fields.Selection(selection = TIPO_PIE, string = 'Tipo Pie')
    ala_1 = fields.Integer('Ala 1')
    ancho = fields.Integer('Ancho')
    ala_2 = fields.Integer('Ala 2')
    grosor = fields.Float('Grosor')
    ala_3 = fields.Integer('Solapa 3')
    longitud = fields.Integer('Longitud')
    ala_4 = fields.Integer('Solapa 4') 
    diametro = fields.Integer('Diámetro')
    gramaje = fields.Integer('Gramaje')
    
    ancho_interior = fields.Integer('Ancho Interior')
    ancho_superficie = fields.Integer('Ancho Superficie')
    
    #varios
    peso_metro_user = fields.Float('Peso Metro', digits = (10,4))
    metros_unidad_user = fields.Float('Metros Unidad', digits = (10,4))
    
    
    #calculados
    peso_metro = fields.Float('Peso Metro', digits = (10,4), readonly = True, compute = "_get_peso_metro")
    metros_unidad = fields.Float('Metros Unidad', digits = (10,4), readonly = True, compute = "_get_valores_referencia")
    se_fabrica = fields.Boolean('Se Fabrica', readonly = True, compute = "_get_valores_referencia")
    j_gram = fields.Integer('J Gram', readonly = True, compute = "_get_valores_referencia")
    j_interior = fields.Integer('J Interior', readonly = True, compute = "_get_valores_referencia")
    j_superficie = fields.Integer('J Superficie', readonly = True, compute = "_get_valores_referencia")
    
    
    @api.depends('type_id',)
    def _get_peso_metro(self):
    
        for record in self:
            peso1 = 0

            #Varios
            if record.type_id.is_varios == True and record.peso_metro_user > 0:
                peso1 = record.peso_metro_user
                
            #Cantonera
            elif record.type_id.is_cantonera == True:
                sumaAlas = record.ala_1 + record.ala_2
                if sumaAlas == 60:
                    peso1 = 385
                elif sumaAlas < 66:
                    peso1 = (425 - 385) / (66 - 60) * (sumaAlas - 60) + 385
                elif sumaAlas == 66:
                    peso1 = 425
                elif sumaAlas < 70:
                    peso1 = (450 - 425) / (70 - 66) * (sumaAlas - 66) + 425
                elif sumaAlas == 70:
                    peso1 = 450
                elif sumaAlas < 76:
                    peso1 = (510 - 450) / (76 - 70) * (sumaAlas - 70) + 450
                elif sumaAlas == 76:
                    peso1 = 510
                elif sumaAlas < 80:
                    peso1 = (535 - 510) / (80 - 76) * (sumaAlas - 76) + 510
                elif sumaAlas == 80:
                    peso1 = 535
                elif sumaAlas < 84:
                    peso1 = (560 - 535) / (84 - 80) * (sumaAlas - 80) + 535
                elif sumaAlas == 84:
                    peso1 = 560
                elif sumaAlas < 90:
                    peso1 = (600 - 560) / (90 - 84) * (sumaAlas - 84) + 560
                elif sumaAlas == 90:
                    peso1 = 600
                elif sumaAlas < 100:
                    peso1 = (700 - 600) / (100 - 90) * (sumaAlas - 90) + 600
                elif sumaAlas == 100:
                    peso1 = 700
                elif sumaAlas < 120:
                    peso1 = (835 - 700) / (120 - 100) * (sumaAlas - 100) + 700
                elif sumaAlas == 120:
                    peso1 = 835
                elif sumaAlas < 140:
                    peso1 = (875 - 835) / (140 - 120) * (sumaAlas - 120) + 835
                elif sumaAlas == 140:
                    peso1 = 875
                elif sumaAlas < 150:
                    peso1 = (940 - 875) / (150 - 140) * (sumaAlas - 140) + 875
                elif sumaAlas == 150:
                    peso1 = 940
                elif sumaAlas < 160:
                    peso1 = (1000 - 940) / (160 - 150) * (sumaAlas - 150) + 940
                elif sumaAlas == 160:
                    peso1 = 1000
                elif sumaAlas < 180:
                    peso1 = (1125 - 1000) / (180 - 160) * (sumaAlas - 160) + 1000
                elif sumaAlas == 180:
                    peso1 = 1125
                elif sumaAlas < 200:
                    peso1 = (1250 - 1125) / (200 - 180) * (sumaAlas - 180) + 1125
                elif sumaAlas == 200:
                    peso1 = 1250
                peso1 = int(peso1 * record.grosor)
                peso1 = peso1 / 10000
                
            #Perfil U
            elif record.type_id.is_perfilu == True:
                sumaAlas = record.ala_1 + record.ancho + record.ala_2 + record.grosor * 2
                if sumaAlas == 60:
                    peso1 = 385
                elif sumaAlas < 66:
                    peso1 = (425 - 385) / (66 - 60) * (sumaAlas - 60) + 385
                elif sumaAlas == 66:
                    peso1 = 425
                elif sumaAlas < 70:
                    peso1 = (450 - 425) / (70 - 66) * (sumaAlas - 66) + 425
                elif sumaAlas == 70:
                    peso1 = 450
                elif sumaAlas < 76:
                    peso1 = (510 - 450) / (76 - 70) * (sumaAlas - 70) + 450
                elif sumaAlas == 76:
                    peso1 = 510
                elif sumaAlas < 80:
                    peso1 = (535 - 510) / (80 - 76) * (sumaAlas - 76) + 510
                elif sumaAlas == 80:
                    peso1 = 535
                elif sumaAlas < 84:
                    peso1 = (560 - 535) / (84 - 80) * (sumaAlas - 80) + 535
                elif sumaAlas == 84:
                    peso1 = 560
                elif sumaAlas < 90:
                    peso1 = (600 - 560) / (90 - 84) * (sumaAlas - 84) + 560
                elif sumaAlas == 90:
                    peso1 = 600
                elif sumaAlas < 100:
                    peso1 = (700 - 600) / (100 - 90) * (sumaAlas - 90) + 600
                elif sumaAlas == 100:
                    peso1 = 700
                elif sumaAlas < 120:
                    peso1 = (835 - 700) / (120 - 100) * (sumaAlas - 100) + 700
                elif sumaAlas == 120:
                    peso1 = 835
                elif sumaAlas < 140:
                    peso1 = (875 - 835) / (140 - 120) * (sumaAlas - 120) + 835
                elif sumaAlas == 140:
                    peso1 = 875
                elif sumaAlas < 150:
                    peso1 = (940 - 875) / (150 - 140) * (sumaAlas - 140) + 875
                elif sumaAlas == 150:
                    peso1 = 940
                elif sumaAlas < 160:
                    peso1 = (1000 - 940) / (160 - 150) * (sumaAlas - 150) + 940
                elif sumaAlas == 160:
                    peso1 = 1000
                elif sumaAlas < 180:
                    peso1 = (1125 - 1000) / (180 - 160) * (sumaAlas - 160) + 1000
                elif sumaAlas == 180:
                    peso1 = 1125
                elif sumaAlas < 200:
                    peso1 = (1250 - 1125) / (200 - 180) * (sumaAlas - 180) + 1125
                elif sumaAlas == 200:
                    peso1 = 1250
                #Añadido
                elif sumaAlas <= 240:
                    peso1 = (1250 - 1125) / (200 - 180) * (sumaAlas - 180) + 1125
                peso1 = int(peso1 * record.grosor)
                peso1 = peso1 / 10000
                
            #Slip Sheet
            elif record.type_id.is_slipsheet == True:
                peso1 = int((record.grosor * 1000 / 1.4 + 30) / 50) * 50
                peso1 = peso1 / 1000
                
            #Solid Board
            elif record.type_id.is_solidboard == True:
                peso1 = int((record.grosor * 1000 / 1.4 + 30) / 50) * 50
                peso1 = peso1 / 1000
                
            #Formato
            elif record.type_id.is_formato == True:
                peso1 = record.gramaje / 1000
                
            #Bobina
            elif record.type_id.is_bobina == True:
                peso1 = record.gramaje / 1000
                
            #Pie de Pallet
            elif record.type_id.is_pieballet == True:
                if record.pie == '1' or record.pie == '2':
                    peso1 = 1.25
                elif record.pie == '3' or record.pie == '4':
                    peso1 = 0.75
                        
            record.peso_metro = peso1
    
    
    
    @api.depends('type_id',)
    def _get_valores_referencia(self):
    
        for record in self:
            se_fabrica = True
            metros = 0
            gram = 0
            interior = 0
            superficie = 0

            #Varios
            if record.type_id.is_varios == True:
                se_fabrica = False
		metros = record.metros_unidad_user
            #Cantonera
            elif record.type_id.is_cantonera == True:
		se_fabrica = True
                metros = record.longitud / 1000
                gram = int((record.grosor * 1000 / 1.4 - 300) / 50) * 50
                interior = int(record.ala_1 + record.ala_2 - record.grosor * 2 - 1)
                superficie = int(((record.ala_1 + record.ala_2 - record.grosor - 1) * 2 + 5) / 5) * 5
                if superficie > 280:
                    superficie = 280
            #Perfil U
            elif record.type_id.is_perfilu == True:
		se_fabrica = False
                metros = record.longitud / 1000
                gram = int((record.grosor * 1000 / 1.4 - 300) / 50) * 50
                interior = int(record.ala_1 + record.ancho + record.ala_2 - 1)
                superficie = int(((record.ala_1 + record.ancho + record.ala_2 - 1 + record.grosor) * 2 + 5) / 5) * 5
                if superficie > 280:
                    superficie = 280
            #Slip Sheets
            elif record.type_id.is_slipsheet == True:
		se_fabrica = True
                sumaAncho = record.ancho
                if record.ala_1 > 0:
                    sumaAncho = sumaAncho + record.ala_1
                if record.ala_2 > 0:
                    sumaAncho = sumaAncho + record.ala_2
                sumaLargo = record.longitud
                if record.ala_3 > 0:
                    sumaLargo = sumaLargo + record.ala_3
                if record.ala_4 > 0:
                    sumaLargo = sumaLargo + record.ala_4
                metros = sumaAncho * sumaLargo / 1000000
                gram = int((record.grosor * 1000 / 1.4 - 300) / 50) * 50
                interior = record.ancho
                if record.ala_1 != None and record.ala_1 > 0:
                    interior = interior + record.ala_1
                if record.ala_2 != None and record.ala_2 > 0:
                    interior = interior + record.ala_2
            #Solid Board
            elif record.type_id.is_solidboard == True:
		se_fabrica = True
                metros = record.ancho * record.longitud / 1000000
                gram = int((record.grosor * 1000 / 1.4 - 300) / 50) * 50
                interior = record.ancho + 30
            #Formato
            elif record.type_id.is_formato == True:
		se_fabrica = False
                metros = record.ancho * record.longitud / 1000000
                gram = record.gramaje
                interior = record.ancho
            #Bobina
            elif record.type_id.is_bobina == True:
		se_fabrica = False
                metros = (record.diametro * record.diametro - 10000) * 0.61 / record.gramaje
                gram = record.gramaje
                interior = record.ancho
                
            #Pie de Pallet
            elif record.type_id.is_pieballet == True:
		se_fabrica = False
                metros = record.longitud / 1000
        
	
            record.se_fabrica = se_fabrica
            record.metros_unidad = metros
            record.j_gram = gram
            record.j_interior = interior
            record.j_superficie = superficie
    
    
    @api.multi
    def create_bom_from_ref(self, bomref):
        for bom in self.env['mrp.bom'].search([('code', '=', bomref),]):
            newbom = bom.copy()
            newbom.code = ''
            newbom.product_tmpl_id = self.id
            break
            
