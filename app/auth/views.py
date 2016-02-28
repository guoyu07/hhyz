# encoding=utf-8
import logging
import io
from datetime import datetime
from hashlib import md5
from .. import db
from . import auth
from code import AuthCode
from flask import render_template, request, url_for, flash, redirect, Response, session, send_file, jsonify
from flask.ext.login import login_required, login_user, logout_user, current_user,current_app
from forms import RegisterForm, LoginForm, InfoForm
from ..models import User,TempAvatar
from ..tools import get_img_url,cut_img
from ..email import send_email


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.values.get('is_request_form', type=bool):
        return render_template('auth/login.html', form=form)
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        # if user is not None and user.verify_password(form.password.data):
        login_user(user, form.remember_me.data)
        next = request.values.get('next')
        return jsonify({'success': True, 'next': next})
    else:
        show_auth = False
        if session.get('login_error_num') > 2:
            show_auth = True
        elif session.get('login_error_num') == None:
            session['login_error_num'] = 1
        else:
            session['login_error_num'] += 1
        error = form.errors.values()[0]
        if form.errors.has_key('verification'):
            error = form.errors['verification']
        return jsonify({'success': False, 'show_auth': show_auth, 'info': error})

#登录页面
@auth.route('/login_view')
def login_view():
    form = LoginForm()
    return render_template('auth/login_view.html', form=form)

#注册新用户
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

#返回验证码
@auth.route('/authcode')
def authcode():
    auth_code, auth_image = AuthCode().get_data()
    session['auth_code'] = auth_code
    out_put = io.BytesIO()
    auth_image.save(out_put, format='JPEG')
    out_put.seek(0)
    return send_file(out_put, mimetype='image/png')

#用户信息页面
@auth.route('/info')
@login_required
def info():
    return render_template('auth/info.html')

#修改用户信息
@auth.route('/edit_info', methods=['GET', 'POST'])
@login_required
def edit_info():
    form = InfoForm()
    if form.validate_on_submit():
        current_user.name = form.name.data
        current_user.phone = form.phone.data
        current_user.gender = form.gender.data
        current_user.age = form.age.data
        current_user.about_me = form.about_me.data
        if session.get('avater_temp') and request.values.get('is_update_avatar',type=bool):
            x=request.values.get('select_x',type=int)
            y=request.values.get('select_y',type=int)
            x2=request.values.get('select_x2',type=int)
            y2=request.values.get('select_y2',type=int)
            path=session['avater_temp']
            url=get_img_url(cut_img(path,(x,y,x2,y2)))
            current_user.avatar=url
            session['avater_temp']=None
        db.session.add(current_user)
        db.session.commit()
        return redirect(url_for('auth.info'))
    return render_template('auth/edit_info.html', form=form)


@auth.route('/collect')
def collect():
    page=request.values.get('page',1,int)
    pagination=current_user.collects.paginate(page,per_page=current_app.config['HHYZ_POSTS_PER_PAGE'],error_out=False)
    posts=pagination.items
    return render_template('auth/collects.html',posts=posts,pagination=pagination)
@auth.route('/logout')
@login_required
def logout():
    url = request.referrer
    logout_user()
    return redirect(url)

#头像上传
@auth.route('/avatar_upload', methods=['GET', 'POST'])
def avatar_upload():
    m = md5()
    img_file = request.files['files[]']
    m.update(img_file.stream.getvalue())
    ext_name=img_file.filename.split('.')[-1]
    path='temp/'+m.hexdigest()+'.'+ext_name
    img_file.save(path)
    t=TempAvatar.query.filter_by(path=path).first()
    if not t:
        t=TempAvatar(path=path)
        db.session.add(t)
        db.session.commit()
    else:
        TempAvatar.query.filter_by(path=path).update({'timestamp':datetime.now()})
        # TempAvatar.update().where(id=t.id)
        db.session.commit()
    session['avater_temp'] = path
    return jsonify({'url': url_for('auth.avatar_temp',name=m.hexdigest()+'.'+ext_name)})
#返回头像缓存
@auth.route('/avatar_temp')
def avatar_temp():
    name=request.values.get('name')
    file=open(current_app.config['abspath']+'/temp/'+name,'r')
    return send_file(file, mimetype='image/png')
