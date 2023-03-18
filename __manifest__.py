{
    'name': 'Employee Helpdesk',
    'sequence': 1,
    'version': '16.0.1.0.0',
    'depends': ['base','website','hr','mail'],

    'data':  ['security/ir.model.access.csv',
              'views/employee_helpdesk.xml',
              'data/helpdesk_website.xml',
              'views/helpdesk_template.xml',
              'views/employee_helpdesk_menu.xml',
              ],

    'installable': True,
    'application': True,
    'auto_install': False,

}
