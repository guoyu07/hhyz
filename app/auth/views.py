# encoding=utf-8
import logging
import io
from .. import db
from . import auth
from code import AuthCode
from flask import render_template, request, url_for, flash, redirect, Response, session, send_file, jsonify
from flask.ext.login import login_required, login_user, logout_user, current_user
from forms import RegisterForm, LoginForm, InfoForm
from ..models import User
from ..email import send_email


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.values.get('is_request_form',type=bool):
        return render_template('auth/login.html', form=form)
    if form.validate_on_submit():
        user=User.query.filter_by(username=form.username.data).first()
        # if user is not None and user.verify_password(form.password.data):
        login_user(user, form.remember_me.data)
        next=request.values.get('next')
        return jsonify({'success': True,'next':next})
    else:
        show_auth = False
        if session.get('login_error_num') > 2:
            show_auth = True
        elif session.get('login_error_num') == None:
            session['login_error_num'] = 1
        else:
            session['login_error_num'] += 1
        error=form.errors.values()[0]
        if form.errors.has_key('verification'):
            error=form.errors['verification']
        return jsonify({'success': False, 'show_auth': show_auth, 'info':error})

@auth.route('/login_view')
def login_view():
    form = LoginForm()
    return render_template('auth/login_view.html',form=form)


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if request.method == 'POST' and form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data,
                    password=form.password.data,
                    avatar=url_for('static', filename='img/default_avatar.png'))
        db.session.add(user)
        db.session.commit()
        # token=user.generate_confirmation_token()
        # send_email(form.email.data,'激活你的账户','auth/email/confirm',user=user,token=token)
        flash(u'注册成功,稍后您的邮箱' + form.email.data + u'会收到一封邮件,请点击激活链接进行激活')
        return redirect(url_for('auth.register_success'))
    return render_template('auth/register.html', form=form)


@auth.route('/register_success')
def register_success():
    return render_template('auth/register_success.html')


@auth.route('/authcode')
def authcode():
    auth_code, auth_image = AuthCode().get_data()
    session['auth_code'] = auth_code
    out_put = io.BytesIO()
    auth_image.save(out_put, format='JPEG')
    out_put.seek(0)
    return send_file(out_put, mimetype='image/png')


@auth.route('/info')
@login_required
def info():
    return render_template('auth/info.html')


@auth.route('/edit_info')
@login_required
def edit_info():
    form = InfoForm()
    if form.validate_on_submit():
        current_user.name = form.name.data
        current_user.phone = form.phone.data
        current_user.gender = form.gender.data
        current_user.age = form.age.data
        current_user.about_me = form.about_me.data
        db.session.add(current_user)
        db.session.commit()
        return redirect(url_for('auth.info'))
    return render_template('auth/edit_info.html', form=form)


@auth.route('/collect')
def collect():
    pass


@auth.route('/logout')
@login_required
def logout():
    url = request.referrer
    logout_user()
    return redirect(url)
