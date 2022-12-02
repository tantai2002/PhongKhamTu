
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin

app = Flask(__name__)
app.secret_key = 'sdlagfjhcbjawdyg2387423837836'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:12345678@localhost/phongkhamtu?charset=utf8mb4'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

app.app_context().push()
db = SQLAlchemy(app=app)
admin = Admin(app = app, name = 'Hệ thống Admin', template_mode='bootstrap4')