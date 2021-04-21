#from fathom.fathom_app import app
#from fathom.fathom_app import app
## BLUEPRINTS IMPORT
##from fathom.dashboard import dashboard
##from fathom.pinned import pinned

## BLUEPRINTS REGISTER
##app.register_blueprint(dashboard)
##app.register_blueprint(pinned)

import os
from flask import copy_current_request_context
from flask_security import current_user, hash_password
from fathom import create_app
from fathom import db
from fathom.auth import user_datastore

env = 'dev'
app = create_app('fathom.config.%sConfig' % env.capitalize())

#Imports current_user from flask_security and via @app.context_processor return value of current_user into "user" and therefore "user" can be used in base.html in {% if user.has_role('') %} 
@app.context_processor
def inject_data():
    return dict(user=current_user)

""" @app.before_first_request
def create_user():
    db.create_all()
    # Create Users
    admin_user = user_datastore.create_user(email='admin@fathom-group.com', password=hash_password('admin123'))
    moderator_user = user_datastore.create_user(email='moderator@fathom-group.com', password=hash_password('superuser123'))
    user_user = user_datastore.create_user(email='user@fathom-group.com', password=hash_password('user123'))
    # Create Roles
    admins_role = user_datastore.create_role(name='admins', description='Administrators')
    moderators_role = user_datastore.create_role(name='moderators', description='Moderators')
    users_role = user_datastore.create_role(name='users', description='Users')
    # Find Roles
    assign_admins_role = user_datastore.find_role("admins")
    assign_moderators_role = user_datastore.find_role("moderators")
    assign_users_role = user_datastore.find_role("users")
    # Find Users
    assign_admin_user = user_datastore.find_user(email='admin@fathom-group.com')
    assign_moderator_user = user_datastore.find_user(email='moderator@fathom-group.com')
    assign_user_user = user_datastore.find_user(email='user@fathom-group.com')
    # Assignments
    assign_admin = user_datastore.add_role_to_user(assign_admin_user, assign_admins_role)
    assign_moderator = user_datastore.add_role_to_user(assign_moderator_user, assign_moderators_role)
    assign_user = user_datastore.add_role_to_user(assign_user_user, assign_users_role)
    db.session.commit() """

## FATHOM MAIN APP START
if __name__ == "__main__":
    app.run()

