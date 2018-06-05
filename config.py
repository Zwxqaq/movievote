#coding:utf-8
"""
配置文件
"""
import os
#基地址，后面用于指定数据库位置方便移植
basedir = os.path.abspath(os.path.dirname(__file__))
#Config类，用于后面进行继承
class Config():
    #密匙，从系统中获许，若没有则用'A TEST SECRET KEY'作为密匙
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'A TEST SECRET KEY'
    #SQL设置，设置为True请求结束会自动commit数据库的变动
    SQLALCHEMY_COMMIT_ON_TEARDOWN = False
    #SQL设置，设置为True会追踪对象的修改并且发送信号
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    #邮箱服务器，使用smtp

    ARTICLES_PER_PAGE = 10

    MAIL_SERVER = "smtp.qq.com"#
    #端口
    MAIL_PORT = 25
    MAIL_USE_TLS = True
    #帐号密码
    MAIL_USERNAME = "603353840@qq.com"#3353840
    MAIL_PASSWORD = "xsvdowgdpazlbddf"#
    #邮件相关设置
    MOVIELOVER_MAIL_SUBJECT_PREFIX = '[MovieLover]'
    MOVIELOVER_MAIL_SENDER = "MovieLover Admin<603353840@qq.com>"
    MOVIELOVER_ADMIN = os.environ.get('MOVIELOVER_ADMIN')

    @staticmethod
    def init_app(app):
        pass
#开发配置，做开发时用此配置，同时打开DEBUG便于调试
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
