# -*- coding: utf-8 -*-
# from odoo import http


# class AddendaExamen(http.Controller):
#     @http.route('/addenda_examen/addenda_examen', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/addenda_examen/addenda_examen/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('addenda_examen.listing', {
#             'root': '/addenda_examen/addenda_examen',
#             'objects': http.request.env['addenda_examen.addenda_examen'].search([]),
#         })

#     @http.route('/addenda_examen/addenda_examen/objects/<model("addenda_examen.addenda_examen"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('addenda_examen.object', {
#             'object': obj
#         })
