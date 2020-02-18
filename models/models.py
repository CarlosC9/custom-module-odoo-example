# -*- coding: utf-8 -*-

from odoo import models, fields, api

class reclamaciones(models.Model):
    _name = 'reclamaciones.reclamaciones'

    id = fields.Char(string="ID", required=True)

    _sql_constraints = [
        ("id_unique", 'UNIQUE(id)', 'El ID de la reclamación debe ser único')
    ]
