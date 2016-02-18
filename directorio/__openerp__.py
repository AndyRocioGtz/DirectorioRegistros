# -*- coding: utf-8 -*-
{
    'name': "Directorio de Registros Publicos",

    'summary': """Directorio""",

    'description':"""
        Control de Directorios
    """,

    'author': "Andrea Magdalena Rocio Gutierrez",
    'website': "andyrociogtz@gmail.com",

    'category': 'Generic Modules',
    'version': '0.1',

    
    'depends': ['base',],

    # Vistas Cargadas
    'data': [            
           'view/registros_directorio_view.xml',
           'view/municipio_view.xml',
           'view/domicilio_view.xml',            
           'view/partido_judicial_view.xml',          
           #'view/equipo_cambios_view.xml',
           #'workflow/equipo_workflow_view.xml',
           #'reportes/reporte_resguardo.xml',
           'security/seguridad.xml',
           'security/ir.model.access.csv'
    ],
  
    'demo': [
        
    ],
    'installable':True,
}