from app import app
from flaskext.mysql import MySQL

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'lucas'
app.config['MYSQL_DATABASE_PASSWORD'] = '123123890890'
app.config['MYSQL_DATABASE_DB'] = 'my_db'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql.init_app(app)