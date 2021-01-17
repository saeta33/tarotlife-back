from flask import Blueprint, request, make_response, jsonify
from api.models import User_score, User_scoreSchema
import json
import logging



# ルーティング設定
user_score_router = Blueprint('user_score_router', __name__)

@user_score_router.route('/user_score/<user_id>', methods=['GET'])

def getUser_scoreList(user_id):
  user_score = User_score.getUser_scoreList(user_id)
  user_score__schema = User_scoreSchema(many=True)

  return make_response(jsonify({
    'code': 200,
    'user_score': user_score_schema.dump(user_score).data
  }))


@user_score_router.route('/user_score', methods=['POST'])
def registUser_score():

  # jsonデータを取得する
  jsonData = json.dumps(request.json)
  user_scoreData = json.loads(jsonData)

  user_score = User_score.registUser_score(user_scoreData)
  user_score_schema = User_scoreSchema(many=True)

  return make_response(jsonify({
    'code': 200,
    'user_score': user_score
  }))
