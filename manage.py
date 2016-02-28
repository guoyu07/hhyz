# /usr/bin/env python
# encoding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import os
from app import create_app,db
from flask.ext.script import Manager,Shell
from flask.ext.migrate import Migrate,MigrateCommand
from app.models import User,Role,Permission,Post,Comment,Classification

app=create_app(os.getenv('FLASK_CONFIG') or 'default')
manager=Manager(app)
migrate=Migrate(app,db)

def make_shell_context():
    return dict(app=app,db=db,User=User,Permission=Permission,Role=Role,
                Post=Post,Comment=Comment,Classification=Classification)

manager.add_command('shell',Shell(make_context=make_shell_context))
manager.add_command('db',MigrateCommand)

if __name__ == '__main__':
    app.config['abspath']=os.getcwd()
    manager.run()

