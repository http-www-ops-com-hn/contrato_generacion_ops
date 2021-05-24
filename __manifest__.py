# -*- coding: utf-8 -*-
{
    'name': "Contratos Empleados",
    'summary': """
           Generacion del contrato para los empleados PDF
        """,
    'author': "Ariel Cerrato",
    'contributors': [
        'dvasquez@guip.com',
        'wcerrato@guip.com',
    ],
    'website': "https://www.guip.com/",
    'category': 'Human Resources',
    'version': '1.0',
    'license': 'OPL-1',
    'data': [
        "reports/convenio_print .xml",
        "reports/convenio_print_view .xml",

        #Nuevas constancias
        "reports/constancia_empleado_view.xml",
        "reports/constancia_salario_empleado_view.xml",
        "reports/constancia_deducciones_empleado_view.xml",

        #convenio
        "reports/contrato_por_hora.xml",
        "views/hr_contract_views.xml",

    ],
    'depends': ['hr','hr_contract','hr_payroll'],
    'installable': True,
    'auto_install': False,
    'application': True,
}