# -*- coding: utf-8 -*-
# from odoo import http


# class Modulos-extras/openAcademy(http.Controller):
#     @http.route('/modulos-extras/open_academy/modulos-extras/open_academy/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/modulos-extras/open_academy/modulos-extras/open_academy/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('modulos-extras/open_academy.listing', {
#             'root': '/modulos-extras/open_academy/modulos-extras/open_academy',
#             'objects': http.request.env['modulos-extras/open_academy.modulos-extras/open_academy'].search([]),
#         })

#     @http.route('/modulos-extras/open_academy/modulos-extras/open_academy/objects/<model("modulos-extras/open_academy.modulos-extras/open_academy"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('modulos-extras/open_academy.object', {
#             'object': obj
#         })
