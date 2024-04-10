# Copyright 2018 Qubiq <info@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Banking Mandate By E-mail",
    "summary": "Send Banking Mandates by e-mail",
    "version": "15.0.1.0.0",
    "category": "Custom",
    "website": "https://www.qubiq.es",
    "author": "QubiQ",
    "license": "AGPL-3",
    "depends": [
        "mail",
        "account_banking_sepa_direct_debit",
    ],
    "data": [
        "views/view_mandate_form.xml",
        "data/email_template_mandate.xml",
        "data/action_server.xml",
    ],
    "application": False,
    "installable": True,
}
