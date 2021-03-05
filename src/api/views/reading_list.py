from flask import Blueprint, request, make_response, jsonify
from api.models import Mreadings, Mreading_listSchema
import json

# ルーティング設定
reading_list_router = Blueprint('reading_list_router', __name__)

@reading_list_router.route('/reading_list/<cat_id>', methods=['GET'])

def getReadingList(cat_id):
  reading_list = Mreadings.getReadingList(cat_id)
  reading_list_schema = Mreading_listSchema(many=True)

  return make_response(jsonify({
    'code': 200,
    'reading_list': reading_list_schema.dump(reading_list).data
  }))

#@karuta_router.route('/karuta', methods=['POST'])
#def registKaruta():

  # jsonデータを取得する
#  jsonData = json.dumps(request.json)
#  karutaData = json.loads(jsonData)

#  karuta = Karuta.registKaruta(karutaData)
#  karuta_schema = KarutaSchema(many=True)

#  return make_response(jsonify({
#    'code': 200,
#    'karuta': karuta
#  }))
