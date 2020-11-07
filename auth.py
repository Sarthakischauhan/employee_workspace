import tkinter as tk
from db import read_data
from flask_bcrypt import Bcrypt
from models import change_status,write_details

crypt=Bcrypt()

class User:
    def __init__(self,detail,status=False):
        if len(detail)==5:
            self.name=detail[1]
            self.password=detail[2]
            self.code,self.dept=detail[3:5]
        elif len(detail)==3:
            self.name=detail[0]
            self.code=detail[1]
            self.dept=detail[2]
        self.authenticated=status

    def __repr__(self):
        return f"User({self.name},{self.code},{self.dept})" 

    @property    
    def is_authenticated(self):
        return self.authenticated

def login(name,passw):
    name,password=name.get(),passw.get()

    query=f"SELECT * FROM employee WHERE code='{name}';"
    user=read_data(query)
    if user:
        current_user=User(user[0])
        if crypt.check_password_hash(current_user.password,password):
            write_details(current_user.code,True)
            change_status()
            return (True,"")
        else :
            return (False,"Wrong Credentials.Please Try Again")
    else :
        return (False,"Wrong Credentials.Please Try Again")

