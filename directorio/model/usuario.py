# -*- coding: utf-8 -*-
from openerp import models,fields, _


"""
'author': "Andrea Magdalena Rocio Gutierrez"
'website': "andyrociogtz@gmail.com"

Este modulo crea el modelo Usuario
"""
#Se crea la clase Usuario
class Usuario(models.Model):
    
	_inherit = 'res.users'

	equipos_ids = fields.Many2one("registros.directorio",
                                    ondelete='set null',string="Oficina", index=True)
	

    