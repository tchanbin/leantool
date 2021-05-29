import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or "chaihongjing"
    SSL_REDIRECT = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True
    FLASKY_PER_PAGE = 10
    SQLALCHEMY_POOL_SIZE = 5

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    # SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://root:11111111@127.0.0.1:3306/management2.0"
    SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://root:11111111@127.0.0.1:4306/wechat"
    # SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://root:11111111@172.20.0.3:3306/wechat"
    # 用于测试是否数据库可以正常连接
    # SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://root:11111111@42.192.213.181:4306/wechat"


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://root:11111111@172.19.0.3:3306/wechat"
    # SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://root:11111111@42.192.213.181:4306/wechat"

    @classmethod
    def init_app(cls, app):
        Config.init_app(app)


class WechatloginConfig(Config):
    DEBUG = True
    Wechat_Login_URI = "https://api.weixin.qq.com/sns/jscode2session?appid=APPID&secret=SECRET&js_code=JSCODE&grant_type=authorization_code"


config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig,
    'production': ProductionConfig,
    "AppSecret": "aeaa22bf24f321482040edca98db6d57",
    "AppID": "wxb7babc153cc97cd2"
}
