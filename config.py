from flask import Flask
from flask_sqlalchemy import SQLAlchemy

host = 'eu-west.connect.psdb.cloud'
usuario = 'rc9por4x38i5a5v51u9e'
passwd = 'pscale_pw_CkLIKjhwIqqB2LGCrLT9UorctRqS736u6GBN8y7rUNy'
bd = 'usuariosdb' 
ssl_mode = "VERIFY_IDENTITY"
ssl = {
    "ca": "/etc/ssl/cert.pem"
}        
        
app = Flask(__name__)

DATABASE_CONNECTION_URI = f'mysql://{usuario}:{passwd}@{host}/{bd}?ssl={ssl}'
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_CONNECTION_URI        
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)        
        
# DATABASE_CONNECTION_URI = f'mysql://{usuario}:{passwd}@{host}/{bd}'
