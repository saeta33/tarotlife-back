from flask import Blueprint, request, make_response, jsonify
from api.models import Karuta, KarutaSchema
import json

# ルーティング設定
karuta_router = Blueprint('karuta_router', __name__)

@karuta_router.route('/karuta/<t_type>', methods=['GET'])

def getKarutaList(t_type):
  karuta = Karuta.getKarutaList(t_type)
  karuta_schema = KarutaSchema(many=True)

  return make_response(jsonify({
    'code': 200,
    'karuta': karuta_schema.dump(karuta).data
  }))

@karuta_router.route('/karuta', methods=['POST'])
def registKaruta():

  # jsonデータを取得する
  jsonData = json.dumps(request.json)
  karutaData = json.loads(jsonData)

  karuta = Karuta.registKaruta(karutaData)
  karuta_schema = KarutaSchema(many=True)

  return make_response(jsonify({
    'code': 200,
    'karuta': karuta
  }))
