import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo13-addons-sygel-technology-sy-account-invoicing",
    description="Meta package for sygel-technology-sy-account-invoicing Odoo addons",
    version=version,
    install_requires=[
        'odoo13-addon-asynchronous_invoice_email',
        'odoo13-addon-bank_accounts_report',
        'odoo13-addon-invoice_inside_account_menu',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 13.0',
    ]
)
