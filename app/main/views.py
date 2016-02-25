# encoding=utf-8
from flask import request,url_for,render_template,current_app,redirect
from . import main
from ..models import Post,Comment,Tag,Classification
#处理主页的请求
@main.route('/',methods=['GET', 'POST'])
def index():
    page=request.values.get('page',1,type=int)
    category=request.values.get('category')
    pagination=Post.query.order_by(Post.id.desc())
    if category:
        pagination=pagination.filter_by(category=category)
    pagination=pagination.paginate(page
                        ,per_page=current_app.config['HHYZ_POSTS_PER_PAGE'],error_out=False)
    posts=pagination.items
    return render_template('index.html',pagination=pagination,posts=posts,category=category)
#处理内容页
@main.route('/post/<int:id>',methods=['GET','POST'])
def post(id):
    post=Post.query.filter_by(id=id).first()
    pagination=post.comments.order_by(Comment.timestamp.desc()).paginate(1,per_page=current_app.config['HHYZ_COMMENTS_PER_PAGE'],error_out=False)
    comments=pagination.items
    print comments[0].parent
    return render_template('post.html',post=post,pagination=pagination,comments=comments)

#站内查询请求
@main.route('/search',methods=['GET', 'POST'])
def search():
    keywords=request.args.get('keywords')
    print keywords
    if not keywords:
       return redirect(url_for('main.index'))
    page=request.args.get('page',1,type=int)
    query=Post.query.search(keywords)
    pagination=query.order_by(Post.id.desc()).\
        paginate(page,per_page=current_app.config['HHYZ_POSTS_PER_PAGE'],error_out=False)
    posts=pagination.items
    return render_template('index.html',pagination=pagination,posts=posts,is_search=True,keywords=keywords)

@main.route('/tags')
def tags():
    name=request.values.get('tag')
    page=request.values.get('page',1,type=int)
    if not name or name=='':
        return redirect(url_for('main.index'))
    pagination=Tag.query.filter_by(name=name).first().posts.paginate(page
                        ,per_page=current_app.config['HHYZ_POSTS_PER_PAGE'],error_out=False)
    posts=pagination.items
    return render_template('index.html',posts=posts,pagination=pagination,tag=name)

@main.route('/classification')
def classification():
    c=request.values.get('c')
    page=request.values.get('page',1,type=int)
    if not c:
        return redirect(url_for('main.index'))
    pagination=Classification.query.filter_by(name=c).first().posts.\
        paginate(page,per_page=current_app.config['HHYZ_POSTS_PER_PAGE'],error_out=False)
    posts=pagination.items
    return render_template('index.html',posts=posts,pagination=pagination,classification=c)

