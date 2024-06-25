# -*- coding: utf-8 -*-
# from odoo import http


# class KnowledgeBase(http.Controller):
#     @http.route('/knowledge_base/knowledge_base', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/knowledge_base/knowledge_base/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('knowledge_base.listing', {
#             'root': '/knowledge_base/knowledge_base',
#             'objects': http.request.env['knowledge_base.knowledge_base'].search([]),
#         })

#     @http.route('/knowledge_base/knowledge_base/objects/<model("knowledge_base.knowledge_base"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('knowledge_base.object', {
#             'object': obj
#         })

