# -*- coding: utf-8 -*-
from odoo import http


class HealthCareVa(http.Controller):
    @http.route('/health_care_va/health_care_va/', auth='public', website=True, type="http", methods=['GET'])
    def index(self, **kw):
        return http.request.render("health_care_va.listing")   # module name.template Id

    @http.route('/test/', auth='public', website=True, type="http", methods=['POST'])
    def test(self, **kw):
        print("......................................................................")
        print(kw)
        print("......................................................................")
        return http.request.render("health_care_va.object")  # module name.template Id

    @http.route('/result/', auth='public', website=True, type="http", methods=['GET'])
    def result(self, **kw):
        print("......................................................................")
        print(kw)
        print("......................................................................")
        return http.request.render("health_care_va.object1")  # module name.template Id

    @http.route('/search', auth='public', website=True, type="http", methods=['GET'])
    def search(self, **kw):
        print("......................................................................")
        print(kw)
        print("......................................................................")
        return http.request.render("health_care_va.object2")  # module name.template Id

    # @http.route('/health_care_va/health_care_va/objects/', auth='public')
    # def list(self, **kw):
    #     return http.request.render('health_care_va.listing', {
    #         'root': '/health_care_va/health_care_va',
    #         'objects': http.request.env['health_care_va.health_care_va'].search([]),
    #     })
    #
    # @http.route('/health_care_va/health_care_va/objects/<model("health_care_va.health_care_va"):obj>/', auth='public')
    # def object(self, obj, **kw):
    #     return http.request.render('health_care_va.object', {
    #         'object': obj
    #     })
