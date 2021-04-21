from .. import db
from flask_security import UserMixin, RoleMixin
#from sqlalchemy.orm import relationship, backref
#from sqlalchemy import Boolean, DateTime, Column, Integer, String, ForeignKey

## Flask-Security
#class RolesUsers(db.Model):
#    __tablename__ = 'roles_users'
#    id = db.Column(db.Integer(), primary_key=True)
#    user_id = db.Column('user_id', db.Integer(), db.ForeignKey('user.id'))
#    role_id = db.Column('role_id', db.Integer(), db.ForeignKey('role.id'))

roles_users = db.Table('roles_users', db.Column('user_id', db.Integer(), db.ForeignKey('user.id')), db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))


class Role(db.Model, RoleMixin):
    __tablename__ = 'role'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

    def __init__(self, name=None, description=None):
        self.name = name
        self.description = description

    def __repr__(self):
#        return '<Role %r>' % (self.name)
        return str('%s').replace('[','').replace(']','') % (self.name)


class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))
    last_login_at = db.Column(db.DateTime())
    current_login_at = db.Column(db.DateTime())
    last_login_ip = db.Column(db.String(100))
    current_login_ip = db.Column(db.String(100))
    login_count = db.Column(db.Integer)
    active = db.Column(db.Boolean())
    fs_uniquifier = db.Column(db.String(255))
    confirmed_at = db.Column(db.DateTime())
    profile_pic = db.Column(db.String(100))
    roles = db.relationship('Role', secondary=roles_users, backref=db.backref('users', lazy='dynamic'))

    def __init__(self, email=None, username=None, password=None, last_login_at=None, current_login_at=None, last_login_ip=None, current_login_ip=None, login_count=None, active=None, fs_uniquifier=None, confirmed_at=None, profile_pic=None, roles=None):
        self.email = email
        self.username = username
        self.password = password
        self.last_login_at = last_login_at
        self.current_login_at = current_login_at
        self.last_login_ip = last_login_ip
        self.current_login_ip = current_login_ip
        self.login_count = login_count
        self.active = active
        self.fs_uniquifier = fs_uniquifier
        self.confirmed_at = confirmed_at
        self.profile_pic = profile_pic
        self.roles = roles

#    def is_authenticated(self):
#        return True

#    def is_active(self):
#        return True

#    def is_anonymous(self):
#        return False

#    def get_id(self):
#        return unicode(self.id)

#    def set_password():
#        pass

#    def check_password():
#        pass

    def __repr__(self):
        return '<User %r>' % (self.username)
###
