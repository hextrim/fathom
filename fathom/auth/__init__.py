from .. import db
from .models import User, Role
#Flask-Security
from flask_security import Security, SQLAlchemyUserDatastore, current_user
from flask_mail import Mail

user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security()
mail = Mail()

def create_module(app, **kwargs):
    security.init_app(app, user_datastore)
    mail.init_app(app)
