from odoo import models, fields

class KnowledgeCategory(models.Model):
    _name = 'knowledge.category'
    _description = 'Knowledge Category'

    name = fields.Char('Name', required=True)
    description = fields.Text('Description')
