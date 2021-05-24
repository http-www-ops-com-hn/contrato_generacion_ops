# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import date,datetime
from dateutil.relativedelta import relativedelta 
from num2words import num2words

class NewFieldsContracts(models.Model):
    _inherit = 'hr.contract'
    # _name = 'new_fields_contract.new_fields_contract'

    text_titulo = fields.Char(string="Profesion u Ocupacion", required=True )
    text_ciudad = fields.Char(string="Ciudad Residencia", required=True )
    txt_gerencia = fields.Boolean('Directores', required=True)
    # hora_contractual = fields.Selection([
    #     ('4','4 Horas'),
    #     ('5','5 Horas'),
    #     ('6','6 Horas'),
    #     ('8','8 Horas'),
    #     ('Permanente','Permanente'),
    #     ], string="Hora contractual", default="")
    employee_address2 = fields.Char(string="Domicilio")
    age = fields.Char(string="Edad del empleado")
    date_of_birth = fields.Date(string="Fecha de nacimiento")
    duracion = fields.Char(string="Duración de contrato")

    @api.onchange('employee_id')
    def _onchange_employee(self):
        self.date_of_birth = self.employee_id.birthday

    @api.onchange('date_of_birth')
    def onchange_employee_age(self):
        for rec in self:
            if rec.date_of_birth:
                d1 = rec.date_of_birth
                d2 = datetime.today().date()
                rd = relativedelta(d2, d1)
                rec.age = num2words(rd.years, lang=self.company_id.partner_id.lang)
            else:
                rec.age = "0"

    @api.onchange('date_start')
    def onchange_contract_date(self):
        for rec in self:
            if rec.date_start:
                d1 = rec.date_start
                d2 = rec.date_end
                rd = relativedelta(d2, d1)
                rec.duracion = str(rd.months) + " Meses"
            else:
                rec.duracion = "Seleccione fecha inicio de contrato"

    @api.onchange('date_end')
    def onchange_contract_date(self):
        for rec in self:
            if rec.date_end:
                d1 = rec.date_start
                d2 = rec.date_end
                rd = relativedelta(d2, d1)
                rec.duracion = str(rd.months) + " Meses"
            else:
                rec.duracion = "Seleccione fecha fin de contrato"

    # dict(self._fields['horas_contrato'].selection).get(self.horas_contrato)
                

    # name = fields.Char()
    # value = fields.Integer()
    # value2 = fields.Float(compute="_value_pc", store=True)
    # description = fields.Text()

    # @api.depends('value')
    # def _value_pc(self):
    #     self.value2 = float(self.value) / 100