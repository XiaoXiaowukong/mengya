# -*- coding: utf-8 -*-
from flask_restful import Api

from controller.home.case_list import CaseList


def load(app):
    api = Api(prefix=app.config["URL_PREFIX"] + '/activity')
    api.add_resource(CaseList, '/list/<string:area_id>')
    api.init_app(app)
