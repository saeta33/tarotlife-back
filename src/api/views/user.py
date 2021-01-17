from flask import Blueprint, request, make_response, jsonify
from api.models import User, UserSchema
import json

# ルーティング設定
user_router = Blueprint('user_router', __name__)

"""
@user_router.route('/user', methods=['GET'])
def getUserList():

  users = User.getUserList()
  user_schema = UserSchema(many=True)

  return make_response(jsonify({
    'code': 200,
    'users': user_schema.dump(users).data
  }))
"""

"""
@user_router.route('/user', methods=['POST'])
def registUser():

  # jsonデータを取得する
  jsonData = json.dumps(request.json)
  userData = json.loads(jsonData)

  user = User.registUser(userData)
  user_schema = UserSchema(many=True)

  return make_response(jsonify({
    'code': 200,
    'user': user
  }))
"""

@user_router.route('/user', methods=['POST'])
def checkUser():

  #jsonデータを取得する
  jsonData = json.dumps(request.json)
  userData = json.loads(jsonData)

  user_res = User.checkUser(userData)
  #user_schema = UserSchema(many=True)

  return make_response(jsonify({
    'code': 200,
    'user_res': user_res
  }))
