from odoo import models, fields, api

class pc(models.Model):
	_name = 'odoo502.pc'
	_description = 'model pc'

	name = fields.Char('ID',required=True)
	nombre = fields.Char(string='Nombre',required=True)
	sistema = fields.Char(string='Sistema',required=True)
