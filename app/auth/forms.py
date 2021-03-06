# encoding=utf-8

from flask_wtf import Form
from wtforms import StringField,PasswordField,BooleanField,SubmitField,ValidationError,TextAreaField,FileField
from wtforms.validators import Length,EqualTo,Email,InputRequired
from ..models import User
from flask import session
# 登陆表单
class LoginForm(Form):
    username=StringField(u'用户名',validators=[InputRequired(message=u'用户名不能为空'),Length(6,64,message=u'用户名长度必须在6到64之间')])
    password=PasswordField(u'密码',validators=[InputRequired(message=u'密码不能为空')])
    verification=StringField(u'验证码')
    remember_me=BooleanField(u'记住登陆')
    submit=SubmitField(u'登陆')
    def validate_verification(self,field):
        if session.get('login_error_num')>2 and session['auth_code'].lower()!=field.data.lower():
            raise ValidationError(message=u'验证码错误')
    def validate_password(self,field):
        user=User.query.filter_by(username=self.username.data).first()
        print self.username,field.data
        if user is  None or not user.verify_password(field.data):
            raise ValidationError(message=u'用户名或密码错误')


# 注册表单
class RegisterForm(Form):
    username=StringField(u'用户名',validators=[InputRequired(message=u'用户名不能为空'),Length(6,64,message=u'用户名长度必须在6到64之间')])
    email=StringField(u'邮箱',validators=[InputRequired(message=u'邮箱不能为空'),Email(message=u'邮箱格式异常')])
    password=PasswordField(u'密码',validators=[InputRequired(message=u'密码不能为空'),EqualTo('password2',message=u'密码不一致')])
    password2=PasswordField(u'重复密码',validators=[InputRequired(message=u'确认密码不能为空')])
    name=StringField(u'用户昵称',validators=[InputRequired(message=u'昵称不能为空')])
    verification=StringField(u'验证码',validators=[InputRequired(message=u'验证码不能为空')])
    agreement=BooleanField(u'同意用户协议',validators=[InputRequired(message=u'必须同意用户协议')])
    submit=SubmitField(u'注册')
    # 邮箱地址验证
    def validate_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError(message=u'邮件地址已存在')
    # 用户名验证
    def validate_username(self,field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError(message=u'用户名已存在')
    def validate_verification(self,field):
        if session['auth_code'].lower()!=field.data.lower():
            raise ValidationError(message=u'验证码错误')


#修改表单

class InfoForm(Form):
    name=StringField(u'昵称')
    phone=StringField(u'电话')
    gender=StringField(u'性别')
    age=StringField(u'年龄')
    about_me=TextAreaField(u'关于我')
    avater=FileField(u'头像')
    submit=SubmitField(u'保存信息')