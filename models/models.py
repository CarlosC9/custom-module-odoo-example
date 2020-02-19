# -*- coding: utf-8 -*-

from odoo import models, fields, api

# Clase
class reclamaciones(models.Model):
    _name = 'reclamaciones.reclamaciones'

    name = fields.Char(string="ID", required=True)
    date = fields.Date(string="Fecha", required=True)
    description = fields.Text(string="Descripción", required=True)
    valid = fields.Boolean(string="Válido", required=True)
    observation = fields.Text(string="Observaciones", required=False)
    client = fields.Many2one(comodel_name="res.partner", string="Cliente", required=True, ondelete="cascade")

    _sql_constraints = [
        ('name_unique', 'UNIQUE(name)', "El id de la reclamación debe ser unico")
    ]

    @api.constrains('name')
    def _check_id(self):
        if len(self.name) > 6:
            raise models.ValidationError('El id no puede ser mas largo de 6 letras')

# Clase heredada
class reclamaciones_clientes(models.Model):
    _name = "res.partner"
    _inherit = "res.partner"

    reclamaciones = fields.One2many(groups="reclamaciones.group_manager, reclamaciones.group_create",comodel_name="reclamaciones.reclamaciones", inverse_name="client", string="Reclamaciones")
