# -*- coding: utf-8 -*-

from odoo import models, fields, api

class reclamaciones(models.Model):
    _name = 'reclamaciones.reclamaciones'

    name = fields.Char(string="ID", required=True)
    date = fields.Date(string="Fecha", required=True)

    _sql_constraints = [
        ('name_unique', 'UNIQUE(name)', "El id de la reclamación debe ser unico")
    ]
