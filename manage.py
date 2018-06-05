#coding:utf-8
import os
from app import create_app, db
from app.model import Movie, Comment, User, Emovie, Ecomment
from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand
from app.email import send_email
app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)
#增加一个命令server
#利用这个命令可以开启flask服务器
manager.add_command("server", Server())
#增加一个命令db，可以控制数据库自动迁移
manager.add_command("db", MigrateCommand)
#增加一个命令shell，可以在命令行进行控制
@manager.shell
def make_shell_context():
    return dict(app = app, db = db, User = User, Movie = Movie, Comment = Comment, Emovie= Emovie, Ecomment = Ecomment)

if __name__  == '__main__':
    manager.run()