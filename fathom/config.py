class Config(object):
    pass

class ProdConfig(object):
    pass

class DevConfig(Config):
    # Statement for enabling the development environment
    DEBUG = True

    # Define the application directory
    import os
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    MAX_CONTENT_PATH = 1024 * 1024 * 1024 * 1024 * 1024

    # Define the database - we are working with
    # SQLite for this example
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'fathom.db')
    #DATABASE_CONNECT_OPTIONS = {}

    # Application threads. A common general assumption is
    # using 2 per available processor cores - to handle
    # incoming requests using one and performing background
    # operations using the other.
    THREADS_PER_PAGE = 4

    # Enable protection agains *Cross-site Request Forgery (CSRF)*
    CSRF_ENABLED     = True

    # Use a secure, unique and absolutely secret key for
    # signing the data.
    CSRF_SESSION_KEY = "secret"

    # Enable Flask-WTF CSRF protection
    WTF_CSRF_ENABLED = True

    # Secret key for signing cookies
    SECRET_KEY = "Or1t3-13t$-i0M4t3"
    #SECRET_KEY = os.urandom(24)

    # Application settings
    APP_NAME = "fathom"
    APP_SYSTEM_ERROR_SUBJECT_LINE = APP_NAME + " system error"

    # Flask-Mail settings
    MAIL_SERVER = "hextrim.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = "admin@hextrim.com"
    MAIL_PASSWORD = "dupajeza123"
    #MAIL_DEFAULT_SENDER

    # Flask-Security
    # https://pythonhosted.org/Flask-Security/configuration.html
    SECURITY_PASSOWRD_HASH = 'bcrypt'
    #SECURITY_PASSWORD_HASH = "pbkdf2_sha512"
    SECURITY_PASSWORD_SALT = SECRET_KEY
    SECURITY_FLASH_MESSAGES = True
    SECURITY_TRACKABLE = True
    SECURITY_REGISTERABLE = True
    SECURITY_EMAIL_SENDER = "admin@hextrim.com"
    #SECURITY_REGISTER_URL
    SECURITY_RECOVERABLE = True
    #SECURITY_RESET_URL
    #SECURITY_CONFIRMABLE = True
    #SECURITY_CONFIRM_URL
    SECURITY_TOKEN_MAX_AGE = 28800
    #SECURITY_UNAUTHORIZED_VIEW
    #app = Flask(__name__, static_url_path='', static_folder='templates/dist', template_folder='templates/dist'), and default folder in the templates is security, no need for override
    SECURITY_LOGIN_USER_TEMPLATE = 'security/login_user.html'
    SECURITY_REGISTER_USER_TEMPLATE = 'security/register_user.html'
    SECURITY_FORGOT_PASSWORD_TEMPLATE = 'security/forgot_password.html'


