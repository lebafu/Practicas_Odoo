# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Alumno(models.Model):
     _name = 'alumno.alumno'
     rut = fields.Char(String='Rut',required=True)
     correo_electronico = fields.Char(String='Correo electronico', required=True)
     carrera = fields.Char(String='Carrera',required=True)
     nombre1 = fields.Char(String='Primer Nombre', required=True)
     nombre2 = fields.Char(String='Segundo Nombre', required=True)
     apellido1 = fields.Char(String='Primer Apellido', required=True)
     apellido2= fields.Char(String='Segundo Apellido', required=True)
     dom_procedencia= fields.Char(String='Domicilio Procedencia', required=True)
     dom_actual= fields.Char(String='Domicilio Actual', required=True)
     telefono=fields.Char(String='Telefono',required=True)
     ano_ingreso = fields.Integer(String='año_ingreso', required=True) #¿????
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100

class Coordinador(models.Model):
    _name = 'coordinador.coordinador'

    nombre = fields.Char(String='Nombre', required=True)
    apellido= fields.Char(String='Apellido', required=True)
    correo_electronico = fields.Char(String='Correo electronico', required=True)

#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100


class Evaluador(models.Model):
    _name = 'evaluador.evaluador'

    nombre = fields.Char(String='Nombre', required=True)
    apellido= fields.Char(String='Apellido', required=True)
    correo_electronico = fields.Char(String='Correo electronico', required=True)
    empresa=fields.Char(String='Empresa', required=True)
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100


class Practica(models.Model):
    _name = 'practica.practica'

    name = fields.Char(String='Nombre', required=True)
    alumno=fields.Many2one('alumno.alumno', String='Alumno');
    coordinador=fields.Many2one('coordinador.coordinador',String='Coordinador')
    evaluador=fields.Many2one('evaluador.evaluador',String='Evaluador')
    #   Empresa
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100