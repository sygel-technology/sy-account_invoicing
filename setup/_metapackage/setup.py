import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo-addons-sygel-technology-sy-account-invoicing",
    description="Meta package for sygel-technology-sy-account-invoicing Odoo addons",
    version=version,
    install_requires=[
        'odoo-addon-bank_accounts_report>=15.0dev,<15.1dev',
        'odoo-addon-followers_mass_invoice_mailing>=15.0dev,<15.1dev',
        'odoo-addon-invoice_inside_account_menu>=15.0dev,<15.1dev',
        'odoo-addon-invoice_line_display_number>=15.0dev,<15.1dev',
        'odoo-addon-invoice_line_label_without_internal_ref>=15.0dev,<15.1dev',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 15.0',
    ]
)
