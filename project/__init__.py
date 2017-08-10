from flask import Flask

app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('flask.cfg')

from project.auth.routes import mod
from project.bucket.routes import mod
from project.api.routes import mod
from project.admin.routes import mod

app.register_blueprint(auth.routes.mod, url_prefix ='/auth')
app.register_blueprint(bucket.routes.mod, url_prefix = '/bucket')
app.register_blueprint(api.routes.mod)
app.register_blueprint(admin.routes.mod)