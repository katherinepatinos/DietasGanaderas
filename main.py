from flask import Flask
from config import Config
from app import appD
from animal import ani
from nutriente import nut
from baseDatos import mysql

app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(appD)
app.register_blueprint(ani)
app.register_blueprint(nut)
mysql.init_app(app)

if __name__ == '__main__':
    app.run(port=8088, debug=True)
