
from flask import Flask
from database import *
from public import public
from admin import admin
from api import api
from staff import staff
from branch import branch
from maintenance import maintenance

app=Flask(__name__)

app.secret_key="abcd"
app.register_blueprint(public)
app.register_blueprint(admin,url_prefix='/admin')
app.register_blueprint(staff,url_prefix='/staff')
app.register_blueprint(maintenance,url_prefix='/maintenance')
app.register_blueprint(branch,url_prefix='/branch')
app.register_blueprint(api,url_prefix='/api')


app.run(debug=True,port=5345,host="0.0.0.0")