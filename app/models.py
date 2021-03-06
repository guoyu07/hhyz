# encoding=utf-8
from datetime import datetime
from . import db
from . import login_manager
from flask.ext.sqlalchemy import BaseQuery
from werkzeug.security import generate_password_hash,check_password_hash
from flask.ext.login import UserMixin,AnonymousUserMixin
class Permission:
    COMMENT = 0x01#发表评论权限
    MODERATE_ARTICLES = 0x02#修改文章权限
    MODERATE_COMMENTS = 0x04#修改评论权限
    ADMINISTER = 0x80#管理员权限

UserPost = db.Table('user_post',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'),primary_key=True),
    db.Column('post_id', db.Integer, db.ForeignKey('posts.id'),primary_key=True)
)

class User(db.Model,UserMixin):
    __tablename__='users'
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(64),unique=True,index=True)#用户名,不可更改,唯一
    email=db.Column(db.String(64),unique=True,index=True)#邮箱,不可更改,唯一
    password_hash=db.Column(db.String(128))#密码的哈希
    permission=db.Column(db.Integer,default=Permission.COMMENT)#用户的权限
    role_id=db.Column(db.Integer,db.ForeignKey('roles.id'))#角色ID
    name=db.Column(db.String(64),default='')#昵称
    phone=db.Column(db.String(13),default='')#电话
    gender=db.Column(db.Integer,default=1)#性别
    age=db.Column(db.String(4),default='保密')#年龄
    confirmed=db.Column(db.Integer,default=0)#是否激活
    about_me=db.Column(db.Text,default='')#个人说明
    avatar=db.Column(db.String(255),default='')#头像路径
    member_since=db.Column(db.DateTime,default=datetime.now)#注册时间
    last_seen=db.Column(db.DateTime,default=datetime.now,onupdate=datetime.now)#最后登录时间
    collects=db.relationship('Post',secondary=UserPost,lazy='dynamic',backref=db.backref('users', lazy='dynamic'))#收藏
    comments=db.relationship('Comment',lazy='dynamic')#评论
    disabled=db.Column(db.Boolean,default=False)#状态不可用

    #设置密码
    @property
    def password(self):
        return AttributeError('获取密码不合法')
    @password.setter
    def password(self,password):
        self.password_hash=generate_password_hash(password)
    #进行密码核对
    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)
    def __init__(self,*args,**kwargs):
        super(User,self).__init__(*args,**kwargs)


    def __repr__(self):
        return '<User %r>' % self.username
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)#角色名称
    default = db.Column(db.Boolean, default=False, index=True)#是否是默认角色
    permissions = db.Column(db.Integer)#权限
    users = db.relationship('User', backref='role')#持有该角色的用户

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
PostTag=db.Table('post_tag',
    db.Column('post_id',db.Integer,db.ForeignKey('posts.id'),primary_key=True),
    db.Column('tag_id',db.Integer,db.ForeignKey('tags.id'),primary_key=True)
)

class PostQuery(BaseQuery):
    #数据库搜索
    def search(self, keywords):
        criteria = []
        for keyword in keywords.split():
            keyword = '%' + keyword + '%'
            criteria.append(db.or_(Post.title.ilike(keyword),
                                   Post.special_title.ilike(keyword),
                                   Post.content.ilike(keyword)))

        q = reduce(db.and_, criteria)
        return self.filter(q)

class Post(db.Model):
    __tablename__='posts'
    id=db.Column(db.Integer,primary_key=True)
    up=db.Column(db.Integer,default=0)#顶的数量
    down=db.Column(db.Integer,default=0)#踩的数量
    title=db.Column(db.String(255))#标题
    collect=db.Column(db.Integer,default=0)#收藏数
    comment_num=db.Column(db.Integer,default=0)#评论数
    special_title=db.Column(db.String(255))#特殊标题
    tags=db.relationship('Tag',secondary=PostTag,backref=db.backref('posts', lazy='dynamic'))#标签
    timestamp=db.Column(db.DateTime,default=datetime.now)#时间戳
    link=db.Column(db.String(255))#直达链接
    comments=db.relationship('Comment',lazy='dynamic')#评论
    content=db.Column(db.Text)#内容
    disabled=db.Column(db.Boolean,default=False)#状态不可用
    category=db.Column(db.String(64))#分类
    img=db.Column(db.String(255))#文章图片
    from_name=db.Column(db.String(64))#来自网站
    from_url=db.Column(db.String(255))#来自网址
    store=db.Column(db.String(64))#商城
    classification=db.relationship('Classification',uselist=False,backref=db.backref('posts',lazy='dynamic'))#小分类
    classification_id=db.Column(db.Integer,db.ForeignKey('classification.id'))
    query_class=PostQuery#设置基础查询器


    def __init__(self,*args,**kwargs):
        super(Post,self).__init__(*args,**kwargs)
    def __repr__(self):
        return '<Post %r>' % self.title

class Tag(db.Model):
    __tablename__='tags'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(64),unique=True)
    def __repr__(self):
        return '<Post %r>' % self.title


class Comment(db.Model):
    __tablename__='comments'
    id=db.Column(db.Integer,primary_key=True)
    content=db.Column(db.Text)#评论内容
    timestamp=db.Column(db.DateTime,default=datetime.now)#时间戳
    up=db.Column(db.Integer,default=0)#顶的数量
    down=db.Column(db.Integer,default=0)#踩的数量
    disabled=db.Column(db.Boolean,default=False)#状态不可用
    parent=db.relationship('Comment',uselist=False,remote_side=[id],cascade='delete')
    user=db.relationship('User',uselist=False)
    parent_id=db.Column(db.Integer,db.ForeignKey('comments.id'))
    post_id=db.Column(db.Integer,db.ForeignKey('posts.id'))
    user_id=db.Column(db.Integer,db.ForeignKey('users.id'))
    def __init__(self,*args,**kwargs):
        super(Comment,self).__init__(*args,**kwargs)
    def __repr__(self):
        return '<Comment %r>' % self.content

class Classification(db.Model):
    __tablename__='classification'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(255),unique=True)
    parent=db.relationship('Classification',uselist=False,remote_side=[id])
    parent_id=db.Column(db.Integer,db.ForeignKey('classification.id'))
    def __init__(self,*args,**kwargs):
        super(Classification,self).__init__(*args,**kwargs)
    def __repr__(self):
        return '<Classification %r>' % self.name

    @staticmethod
    def create():
        names=['电脑数码', '家用电器', '运动户外', '服饰鞋包', '个护化妆', '母婴用品', '日用百货', '食品保健',
               '礼品钟表', '图书音像', '玩模乐器', '办公设备', '家居家装', '汽车用品', '其他分类'];
        for name in names:
            c=Classification.query.filter_by(name=name).first()
            if c is None:
                c=Classification(name=name)
                db.session.add(c)
        db.session.commit()

#头像缓存文件
class TempAvatar(db.Model):
    __tablename__='temp_avatar'
    id=db.Column(db.Integer,primary_key=True)
    path=db.Column(db.String(255),unique=True)
    timestamp=db.Column(db.DateTime,default=datetime.now)







