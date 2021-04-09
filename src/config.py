class SystemConfig:

  DEBUG = True

  import os

  SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}/{db_name}?charset=utf8mb4'.format(**{
      'user': os.environ["dbuser"],
      'password': os.environ["dbpass"],
      'host': 'db',
      'host': os.environ["dbhost"],
      'db_name': os.environ["dbuser"]
  })

Config = SystemConfig
