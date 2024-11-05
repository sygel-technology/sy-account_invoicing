import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo14-addons-sygel-technology-sy-account-invoicing",
    description="Meta package for sygel-technology-sy-account-invoicing Odoo addons",
    version=version,
    install_requires=[
        'odoo14-addon-asynchronous_invoice_email',
        'odoo14-addon-bank_accounts_report',
        'odoo14-addon-followers_mass_invoice_mailing',
        'odoo14-addon-invoice_inside_account_menu',
        'odoo14-addon-invoice_paid_before',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 14.0',
    ]
)
