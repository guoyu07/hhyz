# encoding=utf-8
from flask import request,url_for,render_template
from .. import db
from . import main
from ..auth.forms import LoginForm


@main.route('/')
def index():
    return render_template('index.html')

@main.route('/post/<int:id>')
def post(id):
    return render_template('post.html')

# @main.route('/register',methods=['GET','POST'])
# def register():
#     return render_template('register.html')

@main.route('/info')
def info():
    return render_template('edit_info.html')