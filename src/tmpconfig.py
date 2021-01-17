class SystemConfig:

  DEBUG = True

  SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}/{db_name}?charset=utf8mb4'.format(**{
      'user': 'tarot',
      'password': 'Tarot123#',
      'host': 'db',
      'db_name': 'tarot'
  })

Config = SystemConfig
