# encoding=utf-8
from flask import request,url_for,render_template,current_app
from .. import db
from . import main
from ..auth.forms import LoginForm
from ..models import Post

@main.route('/',methods=['GET', 'POST'])
def index():
    page=request.args.get('page',1,type=int)
    category=request.args.get('category')
    pagination=Post.query.order_by(Post.id.desc())
    if category:
        pagination=pagination.filter_by(category=category)
    pagination=pagination.paginate(page
                        ,per_page=current_app.config['HHYZ_POSTS_PER_PAGE'],error_out=False)
    posts=pagination.items

    return render_template('index.html',pagination=pagination,posts=posts)

@main.route('/post/<int:id>')
def post(id):
    post=Post.query.filter_by(id=id).first()
    return render_template('post.html',post=post)
@main.route('/info')
def info():
    return render_template('edit_info.html')
