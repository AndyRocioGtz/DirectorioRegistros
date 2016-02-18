# -*- coding: utf-8 -*-
from openerp import models,fields, _


"""
'author': "Andrea Magdalena Rocio Gutierrez"
'website': "andyrociogtz@gmail.com"

Este modulo crea el modelo Partido Judicial
"""
#Se crea la clase Control
class PartidoJ(models.Model):
    
    _name = 'partido.judicial' # String crea entidad tomado por odoo 
                                 #para crear tabla en postgres

    name = fields.Char(string="Partido Judicial", required=True)

    municipio_id = fields.Many2one("municipio",
                                    ondelete='set null',string="Municipio", index=True)
