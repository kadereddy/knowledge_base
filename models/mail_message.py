from odoo import models, fields

class MailMessage(models.Model):
    _inherit = 'mail.message'

    action = fields.Char(string='Action')
    user_id = fields.Many2one('res.users', string='User')
    date_created = fields.Datetime(string='Date Created', default=fields.Datetime.now)