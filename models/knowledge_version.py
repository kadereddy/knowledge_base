from odoo import models, fields

class KnowledgeArticleVersion(models.Model):
    _name = 'knowledge.article.version'
    _description = 'Knowledge Article Version'

    article_id = fields.Many2one('knowledge.article', 'Article', required=True, ondelete='cascade')
    name = fields.Char('Title', required=True)
    content = fields.Html('Content', required=True)
    date_created = fields.Datetime('Date Created', default=fields.Datetime.now)
