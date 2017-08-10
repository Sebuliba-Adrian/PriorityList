from flask import Blueprint, render_template

mod = Blueprint('bucket', __name__, template_folder='templates')

@mod.route('/bucket')
def getStuff():
    return render_template('bucket/index.html')