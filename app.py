from flask import Flask
from routes import cargarRutas
from confi import Config
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config.from_object(Config)
# app.config['JSON_SORT_KEYS'] = False
app.json.sort_keys = False
mysql = MySQL(app)
app.mysql = mysql
cargarRutas(app)

app.run(debug=True, port=4000, host='0.0.0.0')