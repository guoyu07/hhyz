from flask import Blueprint

main=Blueprint('main',__name__)

from . import views
from .filter import format_date,slug
from ..models import Post
main.add_app_template_filter(format_date,'format_date')
main.add_app_template_filter(slug,'slug')
@main.app_context_processor
def inject_top_posts():
    top_posts=Post.query.order_by(Post.id.desc()).limit(5).all()
    return dict(top_posts=top_posts)