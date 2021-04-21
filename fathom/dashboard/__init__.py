def create_module(app, **kwargs):
    from .controllers import dashboard_blueprint
    app.register_blueprint(dashboard_blueprint)