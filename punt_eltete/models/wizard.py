﻿
from odoo import fields, models, api
from odoo.exceptions import UserError, ValidationError
from odoo.addons import decimal_precision as dp




class WizardPartnerSaleOrder(models.TransientModel):
    _name = 'wizard.partner.sale.order'
    _description = "Crear un pedido para un cliente"
    
    def _default_partner(self):
        return self.env['res.partner'].browse(self._context.get('active_id'))
    
    partner_id = fields.Many2one('res.partner', string="Cliente", required=True, default=_default_partner, readonly=True)
    
    user_id = fields.Many2one('res.users', string="Comercial", default=lambda self: self.env.user, required=True)
    date = fields.Date('Fecha', default=fields.Date.today(), required=True)
    state_id = fields.Many2one('res.country.state', string="Provincia")
    country_id = fields.Many2one('res.country', string="País")
    
    line_ids = fields.One2many('wizard.partner.sale.order.line', 'wizard_id', string="Líneas")
    
    

    @api.multi
    def create_sale_order(self): 

        num_pallets = 0
        for line in self.line_ids:
            num_pallets = num_pallets + line.num_pallets
            
        for line in self.line_ids:
        
            if line.referencia_cliente_id.state != 'RCL':
                raise ValidationError("Error: La referencia cliente debe estar en estado REFERENCIA CLIENTE")
        
            #if line.attribute_id.get_price(num_pallets, self.state_id, self.country_id) < 0:
            #    raise ValidationError("Error: No hay ofertas para el atributo " + line.attribute_id.name)
        
        
        sale = self.env['sale.order'].create({'partner_id': self.partner_id.id, 
                                              'date_order':self.date, 
                                              'user_id': self.user_id.id,
                                            })
        
        for line in self.line_ids:
        
            #i = 0
            #while i < line.num_pallets:
            #    i = i+1
            
            product_id = None
            for prod in self.env['product.template'].search([('attribute_id', '=', line.attribute_id.id), ('und_pallet', '=', line.oferta_id.und_pallet),]):
                product_id = prod
                
            if product_id == None:
                product_id = self.env['product.template'].create({'name': line.referencia_cliente_id.name + ', ' + line.attribute_id.name, 
                                                                  'type': 'product',
                                                                  'purchase_ok': False,
                                                                  'sale_ok': True,
                                                                  'categ_id': line.referencia_cliente_id.type_id.id,
                                                                  'attribute_id':line.attribute_id.id, 
                                                                  'und_pallet': line.oferta_id.und_pallet,
                                                                 })
            
            
            sale_line = self.env['sale.order.line'].create({'order_id': sale.id, 
                                                'name':product_id.name, 
                                                'product_uom_qty': line.num_pallets,
                                                'price_unit': line.oferta_id.emetro,
                                                'customer_lead': 1,
                                                'product_uom': 1,
                                                'oferta_id': line.oferta_id.id,
                                                'product_id': product_id.product_variant_id.id,
                                               })
            sale_line._compute_tax_id()
    
        return {
            'type': 'ir.actions.act_window',
            'name': "Pedido",
            'res_model': 'sale.order',
            'res_id': sale.id, ### Un Solo ID
            'view_type': 'form',
            'view_mode': 'form',
            'view_id': False,
            'target': 'current',
            #'target': 'new',
            'nodestroy': True,
        }
    
    
    
class WizardPartnerSaleOrder(models.TransientModel):
    _name = 'wizard.partner.sale.order.line'
    
    def _default_partner(self):
        return self.env['res.partner'].browse(self._context.get('active_id'))


    
    partner_id = fields.Many2one('res.partner', string='Cliente', default=_default_partner, readonly=True)
    state_id = fields.Many2one('res.country.state', string="Provincia", related='wizard_id.state_id', store=True, readonly=True)
    country_id = fields.Many2one('res.country', string="País", related='wizard_id.country_id', store=True, readonly=True)
    wizard_id = fields.Many2one('wizard.partner.sale.order', string="Wizard", required=True)
    referencia_cliente_id = fields.Many2one('sale.referencia.cliente', string='Referencia cliente', required=True)
    attribute_id = fields.Many2one('sale.product.attribute', string="Atributo producto", required=True)
    
    num_pallets = fields.Integer(string="Num pallets")
    
    oferta_id = fields.Many2one('sale.offer.oferta', string="Oferta", required=True)
    
    
    
    
    
    
    
    
    
    

    
    