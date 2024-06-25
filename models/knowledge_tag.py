from odoo import models, fields

class KnowledgeTag(models.Model):
    _name = 'knowledge.tag'
    _description = 'Knowledge Tag'

    name = fields.Char('Name', required=True)
