# -*- coding: utf-8 -*-
from openerp import api, exceptions, fields, models, _


"""
'author': "Andrea Magdalena Rocio Gutierrez"
'website': "andyrociogtz@gmail.com"

Este modulo crea el modelo Municipio
"""
#Se crea la clase Departamento
class Municipio(models.Model):
    
    _name = 'municipio' # String crea entidad tomado por odoo 
                                 #para crear tabla en postgres
    code = fields.Integer(string="No. Municipio", required=True)

    name = fields.Char(string="Municipio", required=True) # Campo a generarse en la tabla _name

    registro_id = fields.Many2one("registros.directorio", string="Registro")

   
