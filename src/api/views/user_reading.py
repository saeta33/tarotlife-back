from flask import Blueprint, request, make_response, jsonify
from api.models import Ereadings, Mreadings, MreadingsSchema
import json

# ルーティング設定
user_reading_router = Blueprint('user_reading_router', __name__)

# 問題1問を取得するメソッドへのルーティング。問題と回答済み解答もしくはスプレッドごとテンプレート
@user_reading_router.route('/user_reading/<reading_id>/<user_id>', methods=['GET'])
def getUser_reading(reading_id, user_id):
  user_answer = Ereadings.getUser_reading(reading_id, user_id)
  
  #問題文読み込み
  reading = Mreadings.getReading(reading_id)
  
  jsonData =""
  #問題文がヒットしたときだけJSONをいじる（エラー回避）
  for i in reading:
    reading_schema = MreadingsSchema(many=True)
    jsonData = reading_schema.dump(reading).data
    print("jsonData", jsonData)
    #Ereadingsにユーザの回答があったらテンプレート（デフォルト解答）を上書き
    if user_answer != "NA":
      jsonData[0]["template"] = user_answer
  
  return make_response(jsonify({
    'code': 200,
    'user_reading': jsonData
  }))

#リーディングの結果を記録するメソッドへのルーティング
@user_reading_router.route('/reg_ereading', methods=['POST'])
def registEreading():

  # jsonデータを取得する
  jsonData = json.dumps(request.json) #JSON形式で取得
  reg_ereadingData = json.loads(jsonData) #JSON-->文字列ディクショナリ
  print("user_id, mreading_id", reg_ereadingData['user_id'],reg_ereadingData['mreading_id'])
  ret = Ereadings.registEreading(reg_ereadingData)
  #user_score_schema = User_scoreSchema(many=True)

  return make_response(jsonify({
    'code': 200,
    'registered': ret
  }))
