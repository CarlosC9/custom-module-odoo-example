# -*- coding: utf-8 -*-
from odoo import http

# class Reclamaciones(http.Controller):
#     @http.route('/reclamaciones/reclamaciones/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/reclamaciones/reclamaciones/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('reclamaciones.listing', {
#             'root': '/reclamaciones/reclamaciones',
#             'objects': http.request.env['reclamaciones.reclamaciones'].search([]),
#         })

#     @http.route('/reclamaciones/reclamaciones/objects/<model("reclamaciones.reclamaciones"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('reclamaciones.object', {
#             'object': obj
#         })