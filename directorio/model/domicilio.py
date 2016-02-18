# -*- coding: utf-8 -*-
from openerp import models,fields, _


"""
'author': "Andrea Magdalena Rocio Gutierrez"
'website': "andyrociogtz@gmail.com"

Este modulo crea el modelo Domicilio
"""
#Se crea la clase Control
class Domicilio(models.Model):
    
    _name = 'registros.domicilio' # String crea entidad tomado por odoo 
                                 #para crear tabla en postgres

    name = fields.Char(string="Calle", required=True)

    colonia = fields.Char(string="Colonia", required=True)

    cp = fields.Char(string="Código Postal", required=True)

    municipio_id = fields.Many2one("municipio",
                                    ondelete='set null',string="Municipio", index=True)