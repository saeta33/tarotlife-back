from api.database import db, ma
import random

class User_score(db.Model):

  __tablename__ = 'user_score'
  user_id = db.Column(db.String(10), nullable=True, primary_key=True)
  score = db.Column(db.Integer, nullable=True)
  score_dt = db.Column(db.DateTime, nullable=True)
  game_id = db.Column(db.String(10), nullable=True)

  #def __repr__(self):
    #return '<User_score %r>' % self.user_id

  def getUser_scoreList(user_id):

    user_score_list = db.session.query(User_score).all()

    if user_score_list == None:
      return []
    else:
      return user_score_list

  def registUser_score(user_score):
    print("user_score", user_score)

    record = User_score(
      user_id = user_score['user_id'],
      score = user_score['score'],
      score_dt = user_score['score_dt'],
      game_id = user_score['game_id']
    )

    #insert
    db.session.add(record)
    db.session.commit()

    return user_score

from marshmallow_sqlalchemy import ModelSchema
class User_scoreSchema(ModelSchema):
    class Meta:
      model = User_score
      fields = ('user_id', 'score', 'score_dt', 'game_id')
