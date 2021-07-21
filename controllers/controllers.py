# -*- coding: utf-8 -*-
# from odoo import http


# class ClosePos(http.Controller):
#     @http.route('/close_pos_report/close_pos_report/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/close_pos_report/close_pos_report/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('close_pos_report.listing', {
#             'root': '/close_pos_report/close_pos_report',
#             'objects': http.request.env['close_pos_report.close_pos_report'].search([]),
#         })

#     @http.route('/close_pos_report/close_pos_report/objects/<model("close_pos_report.close_pos_report"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('close_pos_report.object', {
#             'object': obj
#         })
