class SystemConfig:

  DEBUG = True

  SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}/{db_name}?charset=utf8mb4'.format(**{
      'user': 'admin',
      'password': 'tarot123',
      'host': 'database-tarot.ccr7qhhszj2y.ap-northeast-1.rds.amazonaws.com',
      'db_name': 'tarot'
  })

Config = SystemConfig
