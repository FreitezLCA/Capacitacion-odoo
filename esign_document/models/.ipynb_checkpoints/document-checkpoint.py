# -*- coding: utf-8 -*-

from odoo import api, fields, models
from odoo.exceptions import UserError, ValidationError

class DocumentModel(models.Model):
    _name = "esign.document"
    _description = "Model document by E-sign"
    
    name = fields.Char(string="Nombre")
    description = fields.Text(string="Descripcion")
    document = fields.Binary(string="Documento")
    active = fields.Boolean(string="Activo", default=True)
    
    
    type = fields.Selection(string='Tipo de documento', 
                             selection=[('contrato', 'Contrato'),
                                        ('anexo', 'Anexo'),
                                        ('ficha_personal', 'Ficha personal')], 
                             copy=False)
    
    signatory_id = fields.Many2one('hr.employee', string="Firmante")
    #approver_line_ids = fields.One2many('hr.employee', 'document_id', string="Aprobadores")
    approver_ids = fields.Many2many('res.users', string="Aprobadores")
    
    
    @api.onchange('type')
    def _onchange_name(self):
        if self.type != '':            
            self.name = self.type + '/' + self.signatory_id.name
        