# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

class Course(models.Model):
    _inherit = 'sale.order'
    
    session_id = fields.Many2one(comodel_name='academy.session',
                                 string='Related session',
                                 ondelete='set null')
    
    instructor_id = fields.Many2one(string='Session instructor',
                                   related='session_id.instructor_id')
    
    student_ids = fields.Many2many(string='Students',
                                   related='session_id.student_ids')