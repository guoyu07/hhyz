# encoding=utf-8
from datetime import datetime
from . import db
from flask import request,url_for,current_app
from werkzeug.security import generate_password_hash,check_password_hash
from flask.ext.login import UserMixin,AnonymousUserMixin
class User(db.Model,UserMixin):
    __tablename__='users'
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(64),unique=True,index=True)#用户名,不可更改,唯一
    email=db.String(db.String(64),index=True)#邮箱,不可更改,唯一
    password_hash=db.Column(db.String(64))#密码的哈希
    permission=db.Column(db.Integer,default=Permission.COMMENT)#用户的权限
    role_id=db.Column(db.Integer,db.ForeignKey('roles.id'))#角色ID
    name=db.Column(db.String(64),default=username)#昵称
    phone=db.Column(db.String(13))#电话
    gender=db.Column(db.Integer,default=1)#性别
    age=db.Column(db.Integer)#年龄
    confirmed=db.Column(db.Integer)#是否激活
    about_me=db.String(db.Text)#个人说明
    avatar=db.Column(db.String(255))#头像路径
    member_since=db.Column(db.DateTime,default=datetime.utcnow)#注册时间
    last_seen=db.Column(db.DateTime,default=datetime.utcnow)#最后登录时间
    collect=db.relationship('Post',lazy='dynamic')#收藏
    comments=db.relationship('Comment',backref='author',lazy='dynamic')#评论
    disabled=db.Column(db.Boolean,default=False)#状态不可用

    def __init__(self,*args,**kwargs):
        super(User,self).__init__(*args,**kwargs)
    def is_authenticated(self):
        pass
    def is_active(self):
        pass
    def get_id(self):
        pass

    def __repr__(self):
        return '<User %r>' % self.username


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)#角色名称
    default = db.Column(db.Boolean, default=False, index=True)#是否是默认角色
    permissions = db.Column(db.Integer)#权限
    users = db.relationship('User', backref='role', lazy='dynamic')#持有该角色的用户

    @staticmethod
    def insert_roles():
        roles = {
            'User': (Permission.COMMENT, True),
            'Moderator': (Permission.COMMENT |
                          Permission.MODERATE_ARTICLES |
                          Permission.MODERATE_COMMENTS, False),
            'Administrator': (0xff, False)
        }
        for r in roles:
            role = Role.query.filter_by(name=r).first()
            if role is None:
                role = Role(name=r)
            role.permissions = roles[r][0]
            role.default = roles[r][1]
            db.session.add(role)
        db.session.commit()

    def __repr__(self):
        return '<Role %r>' % self.name
class Post(db.Model):
    __tablename__='posts'
    id=db.Column(db.Integer,primary_key=True)
    up=db.Column(db.Integer)#顶的数量
    down=db.Column(db.Integer)#踩的数量
    title=db.Column(db.String)#标题
    tags=db.Column(db.String)#标签(字符串)
    timestamp=db.Column(db.DateTime,default=datetime.utcnow)#时间戳
    link=db.Column(db.String)#直达链接
    comments=db.relationship('Comment',backref='author',lazy='dynamic')#评论
    content=db.Column(db.Text)#内容
    disabled=db.Column(db.Boolean,default=False)#状态不可用
    categories=db.Column(db.String)#分类
    def __init__(self,*args,**kwargs):
        super(Post,self).__init__(*args,**kwargs)

    def __repr__(self):
        return '<Post %r>' % self.title

class Comment(db.Model):
    __tablename__='comments'
    content=db.column(db.Text)#评论内容
    timestamp=db.Column(db.DateTime,default=datetime.utcnow)#时间戳
    up=db.Column(db.Integer)#顶的数量
    down=db.Column(db.Integer)#踩的数量
    disabled=db.Column(db.Boolean,default=False)#状态不可用
    parent=db.relationship('Comment',uselist=False)
    def __init__(self,*args,**kwargs):
        super(Comment,self).__init__(*args,**kwargs)
    def __repr__(self):
        return '<Comment %r>' % self.content


class Permission:
    COMMENT = 0x01#发表评论权限
    MODERATE_ARTICLES = 0x02#修改文章权限
    MODERATE_COMMENTS = 0x04#修改评论权限
    ADMINISTER = 0x80#管理员权限


