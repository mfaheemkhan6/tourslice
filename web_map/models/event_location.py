# -*- coding: utf-8 -*-
from odoo import fields, models, api, _
import ast


class EventLocation(models.Model):
    _name = 'event.location'
    _rec_name = 'latitude'

    point = fields.Char(string='Map')
    latitude = fields.Float(string='Latitude', compute="get_coordinates", store=True)
    longitude = fields.Float(string='longitude', compute="get_coordinates", store=True)
    zoom = fields.Integer(string='Zoom', compute="get_coordinates", store=True)

    @api.depends('point')
    @api.onchange('point')
    def get_coordinates(self):
        for rec in self:
            if rec.point:
                point_dictionary = ast.literal_eval(rec.point)
                if point_dictionary['position']:
                    rec.latitude = point_dictionary['position']['lat']
                    rec.longitude = point_dictionary['position']['lng']
                if point_dictionary['zoom']:
                    rec.zoom = point_dictionary['zoom']
