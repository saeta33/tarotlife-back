from api.database import db, ma
import random
import logging

class Ereadings(db.Model):

  __tablename__ = 'Ereadings'
  id = db.Column(db.Integer, nullable=True, primary_key=True)
  user_id = db.Column(db.Integer, nullable=True)
  mreading_id = db.Column(db.Integer, nullable=True)
  answer= db.Column(db.String(1000), nullable=True)
  created = db.Column(db.DateTime, nullable=True)
  modified = db.Column(db.DateTime, nullable=True)
  
  #def __repr__(self):
    #return '<Karuta %r>' % self.ans

  #生徒の過去の回答を取得
  def getUser_reading(reading_id, user_id):
    
    # select * from Ereadings
    user_reading = db.session.query(Ereadings).\
        filter(Ereadings.mreading_id==reading_id, Ereadings.user_id==user_id).\
        all()
    print("user_reading",user_reading)    
    if len(user_reading) == 0:
      user_answer = "NA"
    else:
      for i in user_reading:
        user_answer = i.answer
    
    return user_answer

  def registEreading(ereading):
  
    check_ereading = db.session.query(Ereadings).\
        filter(Ereadings.mreading_id==ereading['mreading_id'], Ereadings.user_id==ereading['user_id'],).\
        first()
    if check_ereading == None: #同じmreading_id, user_idがなければinsert
      record = Ereadings(
      user_id = ereading['user_id'],
      mreading_id = ereading['mreading_id'],
      answer = ereading['answer'],
      created = ereading['created'],
      modified = ereading['modified']
      )
      #insert
      db.session.add(record)
      db.session.commit()
      print("inserted")
    else: #同じmreading_id, user_idがあればupdate
      check_ereading.answer = ereading['answer']
      check_ereading.modified = ereading['modified']
      db.session.commit()
      print("updated")
      
    return ereading




from marshmallow_sqlalchemy import ModelSchema
class EreadingsSchema(ModelSchema):
    class Meta:
      model = Ereadings
      fields = ('user_id', 'mreading_id', 'answer')
