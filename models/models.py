# -*- coding: utf-8 -*-

from odoo import models, fields, api

_sql_constraints = [
("id_unique", 'UNIQUE(id_reclamaciones)', 'El ID de la reclamación debe ser único')
]

class reclamaciones(models.Model):
    _name = 'reclamaciones.reclamaciones'

    id_reclamaciones = fields.Char(string="ID", required=True)
