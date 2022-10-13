# -*- coding: utf-8 -*-

from odoo import api, fields, models
from odoo.exceptions import UserError, ValidationError

class DocumentModel(models.Model):
    _name = "esign.document"
    _description = "Model document by E-sign"
    
    name = fields.Char(string="Nombre")
    description = fields.Text(string="Descripcion")
    
    file = fields.Binary(string='Documento', required=True)
    file_name = fields.Char(string='Nombre archivo')
    file_view = fields.Binary(string='Documento vista')
    file_upload = fields.Boolean(string="Documento cargado", default=False)
    
    active = fields.Boolean(string="Activo", default=True)
    
    type = fields.Selection(string='Tipo de documento', 
                             selection=[('contrato', 'Contrato'),
                                        ('anexo', 'Anexo'),
                                        ('ficha_personal', 'Ficha personal')], 
                             copy=False,
                             required=True)
    
    state = fields.Selection(string='Estado', 
                             selection=[('draft', 'Borrador'),
                                        ('visa', 'Visado'),
                                        ('sign', 'Firma'),
                                        ('signed', 'Firmado')], 
                             copy=False)
    
    employee_id = fields.Many2one('res.users', string='Firmante')
    #signatory_id = fields.Many2one('res.users', string="Firmante", required=True)
    #approver_ids = fields.Many2many('hr.employee', string="Aprobadores", required=True)
    approver_ids = fields.Many2many('res.users',
                                    domain="[('groups_id.name', '=', 'Esign / Approver')]",
                                    string="Aprobadores")
    
    creator_id = fields.Many2one('res.users', string="Creador")
    is_creator = fields.Boolean(string='Es el creador', compute='_check_is_creator') 
    
    @api.onchange('type','employee_id','file')
    def _onchange_name(self):
        for rec in self:          
            #if rec.employee_id.name and rec.type != '':
                #rec.name = rec.employee_id.name +' / ' + rec.type
                
            if rec.file:
                rec.file_upload = True
                rec.file_view = rec.file
            
                
    @api.model
    def create(self, vals):
        ## Definition
        ## TODO:
        ### validar que approver exista
        if vals['approver_ids'] == []:
            raise ValidationError('Debe seleccionar como minimo un aprobador del documento')
        if vals['employee_id'] == False:
            raise ValidationError('Debe seleccionar el empleado asociado al documento')
        
        ## TODO:
        ### Crear un mantenedor de tipos de documentos asociados a sus respectivas secuencias
        ### Secuencias se reinician anualmente
        if vals['type'] == 'contrato':
            ref = self.env['ir.sequence'].next_by_code('esign.document.contract')
            vals['name'] = ref
        if vals['type'] == 'anexo':
            ref = self.env['ir.sequence'].next_by_code('esign.document.annex')
            vals['name'] = ref
        if vals['type'] == 'ficha_personal':
            ref = self.env['ir.sequence'].next_by_code('esign.document.personal')
            vals['name'] = ref
            
        #vals['creatores_id'] = self.env['res.users'].user
        vals['creator_id'] = self.env.user.id
        vals['state'] = 'draft'
        return super(DocumentModel, self).create(vals)
    
    
    #@api.depends()
    #def _get_current_user(self):
        #for rec in self:
            #rec.creator_id = self.env.user
            
    @api.depends()
    def _check_is_creator(self):
        for rec in self:
            if rec.creator_id.id == self.env.user.id:
                rec.is_creator = True
            else:
                rec.is_creator = False
                
    def button_draft(self):
        self.write({
            'state': "visa"
        })
        
    def button_visa(self):
        self.write({
            'state': "sign"
        })

    def button_cancell_draft(self):
        self.write({
            'state': "draft"
        })
    
    def button_cancell_visa(self):
        self.write({
            'state': "draft"
        })
        
    def button_cancell_sign(self):
        self.write({
            'state': "visa"
        })
        
    def button_approver(self):
        self.write({
            'state': "sign"
        })
        
    def button_sign(self):
        self.write({
            'state': "signed"
        })
        