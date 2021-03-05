from api.database import db, ma
import random
import logging

class Mspreads(db.Model):

  __tablename__ = 'Mspreads'
  id = db.Column(db.Integer, nullable=True,  primary_key=True)
  name= db.Column(db.String(40), nullable=True)
  template = db.Column(db.String(255), nullable=True)

  #def __repr__(self):
    #return '<Karuta %r>' % self.ans

  def getSpareads(sp_id):
    
    # select * from Mreadings
    reading_list = db.session.query(Mspreads).\
        filter(Mreadings.mclassification_id==sp_id).\
        all()

    return spreads


