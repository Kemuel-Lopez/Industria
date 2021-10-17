# -*- coding: utf-8 -*-

from odoo import api, fields, models


class Wizard(models.TransientModel):
    _name = 'openacademy.wizard'
    _description = "Inicio rapido de asitencia a sesiones"

    def _default_sessions(self):
        return self.env['openacademy.session'].browse(self._context.get('active_ids'))

    session_ids = fields.Many2many('openacademy.session',
        string="Sesiones", required=True, default=_default_sessions)
    attendee_ids = fields.Many2many('res.partner', string="Asistencia")

    def subscribe(self):
        for session in self.session_ids:
            session.attendee_ids |= self.attendee_ids
        return {}
