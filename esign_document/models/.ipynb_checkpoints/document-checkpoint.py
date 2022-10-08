# -*- coding: utf-8 -*-

from odoo import api, fields, models
from odoo.exceptions import UserError, ValidationError

class DocumentModel(models.Model):
    _name = "esign.document"
    _description = "Model document by E-sign"
    
    name = fields.Char(string="Nombre")
    description = fields.Text(string="Descripcion")
    
    file = fields.Binary(string='Documento')
    file_name = fields.Char(string='Nombre archivo')
    
    active = fields.Boolean(string="Activo", default=True)
    
    type = fields.Selection(string='Tipo de documento', 
                             selection=[('contrato', 'Contrato'),
                                        ('anexo', 'Anexo'),
                                        ('ficha_personal', 'Ficha personal')], 
                             copy=False,
                             required=True)
    
    state = fields.Selection(string='Estado', 
                             selection=[('draft', 'Borrador'),
                                        ('review', 'Revisión'),
                                        ('sign', 'Firma'),
                                        ('signed', 'Firmado')], 
                             copy=False)
    
    signatory_id = fields.Many2one('hr.employee', string='Firmante', required=True)
    #signatory_id = fields.Many2one('res.users', string="Firmante", required=True)
    #approver_ids = fields.Many2many('hr.employee', string="Aprobadores", required=True)
    approver_ids = fields.Many2many('res.users',
                                    domain="[('groups_id.name', '=', 'Esign / Approver')]",
                                    string="Aprobadores")
    
    
    @api.onchange('type','signatory_id')
    def _onchange_name(self):
        for rec in self:          
            if rec.signatory_id.name and rec.type != '':
                rec.name = rec.signatory_id.name +' / ' + rec.type
                
    @api.model
    def create(self, vals):
        ## Definition
        vals['state'] = 'draft'
        print('override successfully')
        return super(DocumentModel, self).create(vals)
                
    def button_draft(self):
        self.write({
            'state': "review"
        })
        
    def button_review(self):
        self.write({
            'state': "sign"
        })
    
    def button_sign(self):
        self.write({
            'state': "signed"
        })

    def button_cancell(self):
        self.write({
            'state': "signed"
        })
        