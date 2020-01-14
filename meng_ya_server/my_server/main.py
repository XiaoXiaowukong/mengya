# -*- coding: utf-8 -*-
from flask_migrate import MigrateCommand
from flask_script import Manager
from flask import Flask
import controller
# from flask_restful import Api
from flask_login import LoginManager
from flasgger import Swagger
from db.postgres import ext

app = Flask(__name__)
app.config.from_json('%s/config.json' % app.root_path)

login_manager = LoginManager()
login_manager.session_protection = 'strong'
swagger = Swagger(app)
swagger.load_config(app)
login_manager.init_app(app)
ext.load(app)
controller.load(app)
manager = Manager(app)
manager.add_command('db', MigrateCommand)
# ========================
from models.mode_case import CaseModel

if __name__ == '__main__':
    manager.run()
else:
    application = app
