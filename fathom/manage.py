import os
from fathom import create_app #,db, migrate
#from fathom.dashboard.models import User, etc
#from fathom.pinned_connection.models import DbCostam

env = 'dev'
app = create_app('config.%sConfig' % env.capitalize())

@app.shell_context_processor
def make_shell_context():
    return dict(app=app, db=db, migrate=migrate,User=User)