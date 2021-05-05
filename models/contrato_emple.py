# -*- coding: utf-8 -*-
from odoo import api, fields, models
from datetime import date
from datetime import datetime
from datetime import *
import datetime
from odoo.exceptions import UserError, ValidationError
from num2words import num2words
from itertools import *


class contrato_emple(models.Model):
    _inherit = "hr.contract"

    
    text_titulo = fields.Char(string="Profesion u Ocupacion", required=True )
    text_ciudad = fields.Char(string="Ciudad Residencia", required=True )
    txt_gerencia = fields.Boolean('Directores', required=True)


    