# encoding=utf-8
from datetime import datetime
from flask import request,url_for,jsonify,render_template
from flask.ext.login import login_required,current_user,current_app
from .. import db
from ..models import Comment,Post,User,UserPost
from . import api

@api.route('/add_comment',methods=['GET','POST'])
@login_required
def add_comment():
    try:
        parent_id=request.values.get('parent_id',type=int)
        post_id=request.values.get('post_id',type=int)
        content=request.values.get('content')
        comment=Comment(parent_id=parent_id,content=content,post_id=post_id,user=current_user)

        db.session.add(comment)
        db.session.commit()
        return jsonify({'state':'success','username':current_user.username,
                        'time':str(datetime.now().time().strftime("%H:%M:%S")),'avatar':current_user.avatar,
                        })
    except:
        return jsonify({'state':'error'})


@api.route('/del_comment',methods=['GET','POST'])
@login_required
def del_commemt():
    try:
        id=request.args.get('id',type=int)
        comment=Comment.query.filter_by(id=id).first()
        db.session.delete(comment)
        db.session.commit()
        return jsonify({'state':'success'})
    except:
        return jsonify({'state':'error'})


@api.route('/get_comments',methods=['GET','POST'])
def get_comments():
    page=request.values.get('page',1,type=int)
    post_id=request.values.get('post_id')
    pagination=Post.query.filter_by(id=post_id).first().comments.order_by(Comment.timestamp.desc()).paginate(page
                        ,per_page=current_app.config['HHYZ_COMMENTS_PER_PAGE'],error_out=False)
    comments=pagination.items
    return render_template('comment.html',pagination=pagination,comments=comments)

@api.route('/collect',methods=['GET','POST'])
@login_required
def collect():
    id=request.values.get('id')
    post=Post.query.filter_by(id=id).first()
    if not current_user.collects.filter_by(id=id).first():
        current_user.collects.append(post)
        db.session.commit()
    return jsonify({'state':True,'count':post.users.count()})
@api.route('/del_collect',methods=['GET','POST'])
def del_collect():
    id=request.values.get('id')
    post=Post.query.filter_by(id=id).first()
    current_user.collects.remove(post)
    db.session.commit()
    return jsonify({'state':True})