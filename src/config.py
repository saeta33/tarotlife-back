class SystemConfig:

  DEBUG = True

  SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}/{db_name}?charset=utf8mb4'.format(**{
      'user': 'tarot',
      'password': 'Tarot123#',
      #'host': 'db',
      'host': '140.227.199.44:32000',
      'db_name': 'tarot'
  })

Config = SystemConfig
