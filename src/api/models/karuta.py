from api.database import db, ma
import random
import logging

class Karuta(db.Model):

  __tablename__ = 'tarot_desc'
  seq = db.Column(db.Integer, nullable=True,  primary_key=True)
  ans = db.Column(db.String(10), nullable=True)
  keyword1= db.Column(db.String(500), nullable=True)
  keyword2= db.Column(db.String(500), nullable=True)
  keyword3= db.Column(db.String(500), nullable=True)
  keyword4= db.Column(db.String(500), nullable=True)
  keyword5= db.Column(db.String(500), nullable=True)

  #def __repr__(self):
    #return '<Karuta %r>' % self.ans

  def getKarutaList(t_type):
    #乱数でカードを選択
    if t_type=="majour":
         i = random.randint(1,44)
    elif t_type=="court":
         i = random.randint(45,76)
    elif t_type=="suit":
         i = random.randint(77,156)
    else:
         i = random.randint(1,156)
    print("t_type="+t_type)
    print(i)
   
    # select * from karuta_desc
    karuta_list = db.session.query(Karuta).\
        filter(Karuta.seq==i).\
        all()

    if karuta_list == None:
      return []
    else:
      return karuta_list

  def registKaruta(karuta):
    record = Karuta(
      #name = user['name'],
      #address = user['address'],
      #tel = user['tel'],
      #mail = user['mail']
    )

    #insert into tarot_desc(ans, keyword1, keyword2, keyword3, keyword4, keyword5) values(...)
    db.session.add(record)
    db.session.commit()

    return karuta

from marshmallow_sqlalchemy import ModelSchema
class KarutaSchema(ModelSchema):
    class Meta:
      model = Karuta
      fields = ('ans', 'keyword1', 'keyword2', 'keyword3', 'keyword4', 'keyword5')
