import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo12-addons-sygel-technology-sy-account-invoicing",
    description="Meta package for sygel-technology-sy-account-invoicing Odoo addons",
    version=version,
    install_requires=[
        'odoo12-addon-bank_accounts_report',
        'odoo12-addon-invoice_product_name_description',
        'odoo12-addon-invoices_menu_item',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 12.0',
    ]
)
