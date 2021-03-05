from api.database import db, ma
import random
import logging

class Mreadings(db.Model):

  __tablename__ = 'Vreadings'
  id = db.Column(db.Integer, nullable=True,  primary_key=True)
  mclassification_id = db.Column(db.Integer, nullable=True)
  title= db.Column(db.String(500), nullable=True)
  cname = db.Column(db.String(500), nullable=True)
  question = db.Column(db.String(1000), nullable=True)
  correct_answer = db.Column(db.String(1000), nullable=True)
  template = db.Column(db.String(255), nullable=True)

  #def __repr__(self):
    #return '<Karuta %r>' % self.ans

  def getReadingList(cat_id):
    
    # select * from Mreadings
    reading_list = db.session.query(Mreadings).\
        filter(Mreadings.mclassification_id==cat_id).\
        order_by(Mreadings.id).\
        all()

    return reading_list

  def getReading(id):
    print("id",id)
    # select * from Mreadings
    reading = db.session.query(Mreadings).\
        filter(Mreadings.id==id).\
        all()
    return reading


from marshmallow_sqlalchemy import ModelSchema

class Mreading_listSchema(ModelSchema):
    class Meta:
      model = Mreadings
      fields = ('id', 'title', 'cname')

class MreadingsSchema(ModelSchema):
    class Meta:
      model = Mreadings
      fields = ('id', 'title', 'question', 'correct_answer', 'template')
