# encoding=utf-8
import logging
from flask import request,url_for
from .. import db
from . import auth
from flask import render_template,request,url_for,flash,redirect
from flask.ext.login import login_required,login_user,logout_user
from forms import RegisterForm,LoginForm
from ..models import User
from ..email import send_email
@auth.route('/login',methods=['GET','POST'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        print form.username.data
        user=User.query.filter_by(username=form.username.data).first()
        print user
        if user is not None and user.verify_password(form.password.data):
            login_user(user,form.remember_me.data)
            return 'true'
    return render_template('auth/login.html',form=form)
@auth.route('/register',methods=['GET','POST'])
def register():
    form=RegisterForm()
    if request.method=='POST' and form.validate_on_submit():
        user=User(email=form.email.data,
                  username=form.username.data,
                  password=form.password.data)
        db.session.add(user)
        db.session.commit()
        # token=user.generate_confirmation_token()
        # send_email(form.email.data,'激活你的账户','auth/email/confirm',user=user,token=token)
        flash(u'注册成功,稍后您的邮箱'+form.email.data+u'会收到一封邮件,请点击激活链接进行激活')
        return redirect(url_for('auth.register_success'))
    return render_template('auth/register.html',form=form)

@auth.route('/register_success')
def register_success():
    return render_template('auth/register_success.html')

