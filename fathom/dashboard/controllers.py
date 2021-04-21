from flask import Blueprint, render_template

dashboard_blueprint = Blueprint('dashboard_blueprint', __name__, static_url_path='', static_folder='templates/dist', template_folder='template/dist')

@dashboard_blueprint.route('/', methods=['GET'])
def dashboard_view():
    return render_template('index.html')
