import os
from dotenv import load_dotenv
load_dotenv() #carga las valiables de entorno
class Config:
    mysgl_host = os.getenv('MYSQL_HOST')
    mysql_user = os.getenv('MYSQL_USER')
    mysql_password = os.getenv('MYSQL_PASSWORD')
    mysql_db = os.getenv('MYSQL_DB')
    mysql_port = os.getenv('MYSQL_PORT')