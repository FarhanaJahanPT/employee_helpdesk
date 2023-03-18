from odoo import models, fields
from odoo.fields import Date



class EmployeeHelpdesk(models.Model):
    _name = 'employee.helpdesk'
    _rec_name = "employee_id"
    _inherit = 'mail.thread'

    """create a model for employee help desk,so when form submitted record is created in this model"""

    employee_id = fields.Many2one('hr.employee',string="Employee Name")
    email = fields.Char(string="Email",related="employee_id.work_email")
    Phone = fields.Char(string="Phone",related="employee_id.phone")
    category = fields.Selection([
        ('Technical', 'Technical'),
        ('Personal', 'Personal'),
        ('Others', 'Others')],
        string='Category',readonly=True)
    subject = fields.Char(string="Subject",readonly=True)
    description = fields.Char(string="Description",readonly=True)
    employee_manager_id = fields.Many2one(related="employee_id.parent_id",string="Assigned To")
    employee_department_id = fields.Many2one(related="employee_id.department_id",string="Department")
    date = fields.Date(string="Created Date",default=Date.today(),readonly=True)
    state = fields.Selection([
        ('New', 'New'),
        ('Work In Progress', 'Work In Progress'),
        ('Closed', 'Closed')],
        string='State', default="New")
    attach_file = fields.Binary(string="Image",readonly=True)

    def button_in_close(self):
        """Button action for close the issue"""
        self.write({
            'state': "Closed"
        })
    def button_in_progress(self):
        """Button action for progress the issue"""
        self.write({
            'state': "Work In Progress"
        })



