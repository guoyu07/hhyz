# encoding=utf-8
from flask import request,url_for,render_template,current_app
from . import main
from ..models import Post,Comment
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
    return render_template('post.html',post=post,pagination=pagination,comments=comments)
@main.route('/info')
def info():
    return render_template('edit_info.html')

#站内查询请求
@main.route('/search',methods=['GET', 'POST'])
def search():
    keywords=request.args.get('keywords')
    page=request.args.get('page',1,type=int)
    query=Post.query.search(keywords)
    pagination=query.order_by(Post.id.desc()).\
        paginate(page,per_page=current_app.config['HHYZ_POSTS_PER_PAGE'],error_out=False)
    posts=pagination.items
    return render_template('index.html',pagination=pagination,posts=posts,is_search=True,keywords=keywords)

