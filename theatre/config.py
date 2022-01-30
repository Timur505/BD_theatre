
class Config:
    # Данные конфигурации подключения к БД
    dialect = 'postgresql'
    username = 'gaohonipevkoui'
    password = '67c8682a82e4bdbf797a606a0d17a8f9dc4030fae8549e52ee5b1487aec34a80'
    host = 'ec2-54-220-243-77.eu-west-1.compute.amazonaws.com'
    db_name = 'd34lsf136d5756'

    # Настройки для экземляра: секретный ключ запуска и путь к БД
    SQLALCHEMY_DATABASE_URI = f'{dialect}://{username}:{password}@{host}/{db_name}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = '75343b374aa2aaa269e856ad'
