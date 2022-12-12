
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from urllib.parse import quote
from flask_login import LoginManager
from flask_admin import Admin
import cloudinary.uploader
from flask_babelex import Babel
from sqlalchemy import create_engine
# from admin import myAdminIndex

app = Flask(__name__)
app.secret_key = 'sdlagfjhcbjawdyg2387423837836'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:12345678@localhost/phongkham?charset=utf8mb4'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['DSKHAM_KEY'] = 'dsKham'

# engine = create_engine("mysql+pymysql://root:12345678@localhost/phongkham?charset=utf8mb4", pool_pre_ping=True)

# cloudinary.config(cloud_name='dxxwcby8l',
#                     api_key='448651448423589',
#                   api_secret='ftGud0r1TTqp0CGp5tjwNmkAm-A')

cloudinary.config( 
  cloud_name = "dk06ufcxa", 
  api_key = "868714845115272", 
  api_secret = "58_Sskgnw9dey_teBySWeQhBfQU" 
)


admin = Admin(app = app, name = 'Phòng Khám Tư', template_mode='bootstrap4')
login = LoginManager(app=app)
app.app_context().push()
db = SQLAlchemy(app=app)
# admin = Admin(app = app, name = 'Phòng Khám Tư', template_mode='bootstrap4', index_view=myAdminIndex())
babel = Babel(app=app)

@babel.localeselector
def load_locale():
    return "vi"