import os
import json

with open('/etc/flask_blog_config.json') as config_file:
    config = json.load(config_file)


class Config:
    SECRET_KEY = config.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = config.get('SQLALCHEMY_DATABASE_URI')
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
<<<<<<< HEAD
    MAIL_DEFAULT_SENDER = config.get('EMAIL_USER')
    
    MAIL_USERNAME = config.get('EMAIL_USER')
    MAIL_PASSWORD = config.get('EMAIL_PASS')
=======
    MAIL_USERNAME = "ramilraleskerov@gmail.com" #os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = "TimeTo1mprove" #os.environ.get('EMAIL_PASS')
>>>>>>> e9fdd74e256f36e89d5a8078b63174eaa0f60cc4
