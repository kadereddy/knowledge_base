from odoo import models, fields

class KnowledgeArticleLog(models.Model):
    _name = 'knowledge.article.log'
    _description = 'Knowledge Article Log'

    article_id = fields.Many2one('knowledge.article', 'Article', required=True, ondelete='cascade')
    action = fields.Selection([
        ('viewed', 'Viewed'),
        ('modified', 'Modified'),
        ('archived', 'Archived'),
        ('restored', 'Restored'),
    ], string='Action', required=True)
    user_id = fields.Many2one('res.users', 'User', required=True)
    description = fields.Text('Description')
    date_created = fields.Datetime('Date Created', default=fields.Datetime.now)
