# encoding=utf-8
from datetime import datetime
from flask import request,url_for,jsonify,render_template
from flask.ext.login import login_required,current_user,current_app
from .. import db
from ..models import Comment,Post,User
from . import api

@api.route('/add_comment',methods=['GET','POST'])
@login_required
def add_comment():
    try:
        parent_id=request.args.get('parent_id',type=int)
        content=request.args.get('content')
        post_id=request.args.get('post_id',type=int)
        comment=Comment(parent_id=parent_id,content=content,post_id=post_id)
        db.session.add(comment)
        db.session.commit()
        print 'sfdsfds'
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


@api.route('/get_comment',methods=['GET','POST'])
def get_comment():
    page=request.args.get('page',1,type=int)
    pagination=Comment.query.order_by(Comment.id.desc()).paginate(page
                        ,per_page=current_app.config['HHYZ_POSTS_PER_PAGE'],error_out=False)
    comments=pagination.items
    return render_template('comment.html',pagination=pagination,comments=comments)