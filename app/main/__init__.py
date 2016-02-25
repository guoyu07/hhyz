from flask import Blueprint

main=Blueprint('main',__name__)

from . import views
from ..models import Post,Classification

@main.app_context_processor
def inject_top_posts():
    top_posts=Post.query.order_by(Post.id.desc()).limit(5).all()
    return dict(top_posts=top_posts)

@main.app_context_processor
def inject_class():
    classifications=Classification.query.all()
    return dict(classifications=classifications)