from odoo import models, fields, api, _

class KnowledgeArticle(models.Model):
    _name = 'knowledge.article'
    _description = 'Knowledge Article'
    _inherit = ['mail.thread']

    name = fields.Char('Title', required=True)
    category_id = fields.Many2one('knowledge.category', 'Category', required=True)
    tag_ids = fields.Many2many('knowledge.tag', string='Tags')
    author_id = fields.Many2one('res.users', 'Author', default=lambda self: self.env.user, track_visibility='onchange')
    version_ids = fields.One2many('knowledge.article.version', 'article_id', string='Versions')
    is_archived = fields.Boolean('Archived', default=False)
    attachment_ids = fields.Many2many('ir.attachment', string='Attachments')
    content = fields.Text(string='Content')
    comment_ids = fields.One2many('mail.message', 'res_id', domain=[('model', '=', 'knowledge.article')], string="Comments")
    log_ids = fields.One2many('mail.message', 'res_id', domain=[('model', '=', 'knowledge.article')], string="Logs")


    def write(self, vals):
        # Create a new version before updating the article
        for article in self:
            if 'content' in vals or 'name' in vals:
                self.env['knowledge.article.version'].create({
                    'article_id': article.id,
                    'content': article.content,
                    'name': article.name,
                })
                # Log the modification
                self.env['knowledge.article.log'].create({
                    'article_id': article.id,
                    'action': 'modified',
                    'user_id': self.env.user.id,
                    'description': _("Article '%s' modified") % article.name,
                })
        return super(KnowledgeArticle, self).write(vals)


    def action_archive(self):
        for article in self:
            article.is_archived = True
            # Log the archiving
            self.env['knowledge.article.log'].create({
                'article_id': article.id,
                'action': 'archived',
                'user_id': self.env.user.id,
                'description': _("Article '%s' archived") % article.name,
            })


    def action_restore_version(self, version_id):
        version = self.env['knowledge.article.version'].browse(version_id)
        if version:
            self.write({
                'name': version.name,
                'content': version.content,
            })
            # Log the restoration
            self.env['knowledge.article.log'].create({
                'article_id': self.id,
                'action': 'restored',
                'user_id': self.env.user.id,
                'description': _("Article '%s' restored to version '%s'") % (self.name, version.name),
            })


    def action_view_article(self):
        for article in self:
            # Log the consultation
            self.env['knowledge.article.log'].create({
                'article_id': article.id,
                'action': 'viewed',
                'user_id': self.env.user.id,
                'description': _("Article '%s' viewed") % article.name,
            })
