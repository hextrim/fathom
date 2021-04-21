#import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# Required for Flask-Security TRACKABLE
from werkzeug.middleware.proxy_fix import ProxyFix

#, render_template, request, url_for, flash, copy_current_request_context, redirect, jsonify, Blueprint
# Required for Flask-Security TRACKABLE
# This is for SSE protocol
#import gevent
#from gevent import monkey
##from gevent.pywsgi import WSGIServer
#monkey.patch_all()


db = SQLAlchemy()
migrate = Migrate()

#app = Flask(__name__, static_url_path='', static_folder='templates/dist', template_folder='templates/dist')

def page_not_found(error):
    return render_template('404.html'), 404

def create_app(object_name):
    #from .dashboard.controllers import dashboard_blueprint
    #from .pinned_connection.controllers import pinned_connection_blueprint

    app = Flask(__name__, static_url_path='', static_folder='templates/dist', template_folder='templates/dist')
    app.config.from_object(object_name)
    app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1)
    db.init_app(app)
    migrate.init_app(app,db)
    #from .auth import create_module as auth_create_module
    from .auth import create_module as auth_create_module
    from .dashboard import create_module as dashboard_create_module
    from .pinned_connection import create_module as pinned_connection_create_module
    auth_create_module(app)
    dashboard_create_module(app)
    pinned_connection_create_module(app)
    #app.register_blueprint(dashboard_blueprint)
    #app.register_blueprint(pinned_connection_blueprint)
    #app.register_error_handler(404, page_not_found)
    #db.create_all() <-- does not work here
    return app




#Required for Flask-Security TRACKABLE

