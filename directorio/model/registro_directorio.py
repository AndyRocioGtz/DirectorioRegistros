# -*- coding: utf-8 -*-
from openerp import api, exceptions, fields, models, _

"""
'author': "Andrea Magdalena Rocio Gutierrez"
'website': "andyrociogtz@gmail.com"

Este modulo crea el modelo Registros
"""
#Se crea la clase Registros
class Registros(models.Model):
    
    _name = 'registros.directorio' # String crea entidad tomado por odoo 
                                   #para crear tabla en postgres

    name = fields.Char(readonly = True, string="ID")

    responsable_id = fields.Many2one("res.users", string="Responsable", required=True)

    municipio_id = fields.Many2one("municipio",
                                    ondelete='set null',string="Municipio", index=True)

    municipio_ids = fields.One2many("municipio", "registro_id", string="Partido Judicial", required=True)

    domicilio_id = fields.Many2one("registros.domicilio", string="Calle", required=True)
    
    telefono_rp = fields.Char(string="Teléfono del Registro Público", required=True)
    
    tel_particular = fields.Char(string="Teléfono Particular")

    correo = fields.Char(string="E-mail", required=True)
