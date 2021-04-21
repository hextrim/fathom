def create_module(app, **kwargs):
    from .controllers import pinned_connection_blueprint
    app.register_blueprint(pinned_connection_blueprint)