# Copyright 2018 Qubiq <info@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models


class AccountBankingMandate(models.Model):
    _inherit = 'account.banking.mandate'

    def action_mandate_send(self):
        '''
        This function opens a window to compose an email,
        with the edi sale template message loaded by default
        '''
        self.ensure_one()
        try:
            template_id = self.env.ref(
                'banking_mandate_by_email.email_template_banking_mandate'
            ).id
        except ValueError:
            template_id = False
        try:
            compose_form_id = self.env.ref(
                'mail.email_compose_message_wizard_form'
            ).id
        except ValueError:
            compose_form_id = False

        ctx = {
            'default_model': 'account.banking.mandate',
            'default_res_id': self.ids[0],
            'default_use_template': bool(template_id),
            'default_template_id': template_id,
            'default_composition_mode': 'comment',
            'mark_so_as_sent': True,
            'force_email': True
        }
        return {
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'mail.compose.message',
            'views': [(compose_form_id, 'form')],
            'view_id': compose_form_id,
            'target': 'new',
            'context': ctx,
        }
