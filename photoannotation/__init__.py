from flask import Flask
import pymysql
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SECRET_KEY'] = 'edfaf0ea54d28cf8d331d4f951fbfdbe'
connection = pymysql.connect("localhost", "root", "", "photoannotation")
bcrypt = Bcrypt(app)


from photoannotation import routes