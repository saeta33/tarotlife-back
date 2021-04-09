from api.database import db, ma
import hashlib

class User(db.Model):
  __tablename__ = 'musers'
  id = db.Column(db.Integer, primary_key=True)
  password = db.Column(db.String(50), nullable=False)
  usrmail= db.Column(db.String(50), nullable=True)

  #def __repr__(self):
  #  return '<User %r>' % self.name

  def checkUser(userData):
    sha1 = hashlib.sha1(('qwertyuiopasdfghjklzxcvbnm'+userData['pwd']).encode('utf-8')).hexdigest()
    # select * from users
    user_res = db.session.query(User).\
    filter(User.usrmail==userData['mail']).\
    filter(User.password==sha1).\
    all()
    
    print(userData['mail'])
    print(userData['pwd'])
    print(sha1)
    print("len",len(user_res))

    return user_res

  #def getUserList():
    # select * from users
  #  user_list = db.session.query(User).all()
  #  print(user_list)
  #  if user_list == None:
  #    return []
  #  else:
  #    return user_res

 # def registUser(user):
 #   record = User(
 #     name = user['name'],
 #     address = user['address'],
 #     tel = user['tel'],
 #     mail = user['mail']
 #   )

    # insert into users(name, address, tel, mail) values(...)
 #   db.session.add(record)
 #   db.session.commit()

 #   return user

from marshmallow_sqlalchemy import ModelSchema
class UserSchema(ModelSchema):
    class Meta:
      model = User
      fields = ('id', 'usrmail')
