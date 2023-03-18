from odoo import http
from odoo.http import request
import base64


class WebsitePage(http.Controller):
    """
        By clicking menu directed to a form so first of all need to set a route for a menu . here sets /helpdesk as a
        link for menu,then pass this link to the xml of menu and also return id of website template.
    """
    @http.route('/helpdesk', type='http', auth='public', website=True)
    def web_page_helpdesk(self, **kw):
        employee_id = request.env['hr.employee'].sudo().search([])

        return request.render('employee_helpdesk.website_page_employee_helpdesk', {'employee_id':employee_id,})


class WebsitePageThanks(http.Controller):

    """ for creating datas to a model get values from website using kw.get() then pass this to a dictionary,then creates
     on corresponding model.Here returns id of thanks website page,so get corresponding link which pass on xml"""

    @http.route('/employee/helpdesk/', type='http', auth='public', website=True)
    def create_web_page_helpdesk(self, post=None, **kw):
        print(kw.get('file'))
        vals = request.env['employee.helpdesk'].sudo().create({
            'employee_id': kw.get('employee_id'),
            'email': kw.get('email_id'),
            'Phone': kw.get('phone_num'),
            'category': kw.get('category'),
            'subject': kw.get('subject'),
            'description': kw.get('description'),

        })
        file_name = kw.get('attach_file').filename
        file = kw.get('attach_file')
        request.env['ir.attachment'].sudo().create({
            'name': file_name,
            'type': 'binary',
            'datas': base64.b64encode(file.read()),
            'res_model': 'employee.helpdesk',
            'res_id': vals.id,
            'res_field' : 'attach_file'
        })




        print(vals)
        value = {
            'vals': vals,
        }
        return request.render('employee_helpdesk.website_helpdesk_thanks_menu', value)