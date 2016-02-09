# encoding=utf-8
from flask import request,url_for
from .. import db
from . import main


@main.route('/')
def index():
    return '<h1>你好</h1>'