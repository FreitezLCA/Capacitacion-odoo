# -*- coding: utf-8 -*-

from odoo import api, fields, models

class ApproverModel(models.Model):
    _inherit = 'res.users'
    
    document_ids = fields.Many2many('esign.document', string="Documentos")