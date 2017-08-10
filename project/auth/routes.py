from flask import Blueprint, render_template
mod = Blueprint('auth', __name__,template_folder='templates')

@mod.route('/auth')
def auth():
    return render_template('auth/index.html')
