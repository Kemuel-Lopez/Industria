# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class modulos-extras/open_academy(models.Model):
#     _name = 'modulos-extras/open_academy.modulos-extras/open_academy'
#     _description = 'modulos-extras/open_academy.modulos-extras/open_academy'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
