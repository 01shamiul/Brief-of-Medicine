# -*- coding: utf-8 -*-

from odoo import models, fields, api


class health_care_va(models.Model):
    _name = 'health_care_va.health_care_va'
    _description = 'health_care_va.health_care_va'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100
