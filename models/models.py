# -*- coding: utf-8 -*-

from odoo import models, fields, api

class AlumnoRequest(models.Model):
     _name = 'alumno.request' #Tabla en BD alumno_alumno
    _inherit = ['mail.thread']
    _description = "Alumno Request"

     rut = fields.Char(String='Rut',required=True)
     email = fields.Char(String='email', required=True)
     carrera = fields.Char(String='Carrera',required=True)
     nombre1 = fields.Char(String='Primer Nombre', required=True)
     nombre2 = fields.Char(String='Segundo Nombre', required=True)
     apellido1 = fields.Char(String='Primer Apellido', required=True)
     apellido2= fields.Char(String='Segundo Apellido', required=True)
     dom_procedencia= fields.Char(String='Domicilio Procedencia', required=True)
     dom_actual= fields.Char(String='Domicilio Actual', required=True)
     telefono=fields.Char(String='Telefono',required=True)
     ano_ingreso = fields.Integer(String='año_ingreso', required=True) #¿????

    @api.onchange('email')
    def _onchange_email(self):
        """
        Email: YOURNAME@YOURCOMPANY.COM
        Website: http://www.YOURCOMPANY.COM
        :return:
        """
        # return {
        #     'domain': {'other_id': [('partner_id', '=', partner_id)]},
        #     'warning': {'title': "Warning", 'message': "What is this?"},
        # }
        result = {}
        if self.email:
            # self.website = 'http://www.%s' % (self.email.split('@')[1])
            result.update({
                'value': {
                    'website': 'http://www.%s' % (self.email.split('@')[1])
                },
                'warning': {
                    'title': 'Congrates!',
                    'message': 'You have added an email!',
                },
                'domain': {
                    'ano_ingreso': [('ano_ingreso', '>', 1997)],
                }
            })

        return result

    # _sql_constraints is working on DB level and you can find it in the table:
    # \d TABLE_NAME
    # SQL Constraints can use to rules: unique & check
    _sql_constraints = [
        ('unique_email', 'unique(email)', 'El Email debe ser unico'),
    ]

    @api.constrains('email')
    def _check_email(self):
        """
        Constrains will check / triggered for the listed fields only in creation and updating.
        @api.constraints will work on the application level
        :return:
        """
        if self.email.endswith('gmail.com'):
            raise ValidationError("Gmail is not accepted!")
        if self.email.endswith('yahoo.com'):
            raise ValidationError("Yahoo is not accepted!")

    @api.multi
    def confirm_request(self):
        self.state = 'confirm'

    @api.multi
    def validate_request(self):
        self.state = 'validate'

    @api.multi
    def refuse_request(self):
        self.state = 'refuse'

    @api.multi
    def approve_request(self):
        self.state = 'approved'

#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100

#class Coordinador(models.Model):
#    _name = 'coordinador.coordinador'

#    nombre = fields.Char(String='Nombre', required=True)
#    apellido= fields.Char(String='Apellido', required=True)
#    correo_electronico = fields.Char(String='Correo electronico', required=True)

#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100


#class Evaluador(models.Model):
#    _name = 'evaluador.evaluador'
#
#    nombre = fields.Char(String='Nombre', required=True)
#    apellido= fields.Char(String='Apellido', required=True)
#    correo_electronico = fields.Char(String='Correo electronico', required=True)
#    empresa=fields.Char(String='Empresa', required=True)
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100


#class Practica(models.Model):
#    _name = 'practica.practica'

#    name = fields.Char(String='Nombre', required=True)
#    alumno=fields.Many2one('alumno.alumno', String='Alumno');
#    coordinador=fields.Many2one('coordinador.coordinador',String='Coordinador')
#    evaluador=fields.Many2one('evaluador.evaluador',String='Evaluador')
    #   Empresa
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
