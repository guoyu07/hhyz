from flask import Blueprint

main=Blueprint('main',__name__)

from . import views
from .filter import format_date,slug
main.add_app_template_filter(format_date,'format_date')
main.add_app_template_filter(slug,'slug')