{
    'name': "Invoice Number In Header",
    'summary': """
        Add custom text to invoice headers""",
    'description': """
        Adds the invoice number to the hgeader of the invoice from page two and onwards
    """,
    'author': "Lasse Larsson, Kubang AB",
    'website': "http://www.kubang.eu",
    'category': 'Accounting',
    'version': '1.0',
    'depends': ['account'],
    'data': [
        'views/invoice_header_views.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}                            