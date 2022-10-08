# -*- coding: utf-8 -*-

from odoo import api, fields, models

class SignatoryModel(models.Model):
    _name = "esign.signatory"
    _description = "Model signatory by E-sign"
    
    name = fields.Char(string="Nombre", related='signatory_id.name')
    signatory_id = fields.Many2one('hr.employee', string="Firmante")
    active = fields.Boolean(string="Activo", default=True)
    
    signature = fields.Boolean(string="Firmado", default=False)