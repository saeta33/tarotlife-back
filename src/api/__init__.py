from flask import Flask, request, make_response, jsonify
#from flask import Response, abort, render_template  #flask_login用
from .views.user import user_router
from .views.karuta import karuta_router
from .views.user_score import user_score_router
from .views.reading_list import reading_list_router
from .views.user_reading import user_reading_router
from flask_cors import CORS, cross_origin
from api.database import db
import config
#from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin
from collections import defaultdict

def create_app():
  app = Flask(__name__)
  ################flask_login
  """
  login_manager = LoginManager()
  login_manager.init_app(app)
  app.config['SECRET_KEY'] = "secret"
  app.config['EXPLAIN_TEMPLATE_LOADING'] = True


  class User(UserMixin):
    def __init__(self, id, name, password):
        self.id = id
        self.name = name
        self.password = password

  # ログイン用ユーザー作成
  users = {
    1: User(1, "user01", "password"),
    2: User(2, "user02", "password")
  }

  # ユーザーチェックに使用する辞書作成
  nested_dict = lambda: defaultdict(nested_dict)
  user_check = nested_dict()
  for i in users.values():
    user_check[i.name]["password"] = i.password
    user_check[i.name]["id"] = i.id

  @login_manager.user_loader
  def load_user(user_id):
    return users.get(int(user_id))

  @app.route('/')
  def home():
      return Response("home: <a href='/login/'>Login</a> <a href='/protected/'>Protected</a> <a href='/logout/'>Logout</a>")

  # ログインしないと表示されないパス
  @app.route('/protected/')
  @login_required
  def protected():
      return Response('''
      protected<br />
      <a href="/logout/">logout</a>
      ''')

  # ログインパス
  @app.route('/login/', methods=["GET", "POST"])
  def login():
    if(request.method == "POST"):
      # ユーザーチェック
      if(request.form["username"] in user_check and request.form["password"] == user_check[request.form["username"]]["password"]):
        # ユーザーが存在した場合はログイン
        login_user(users.get(user_check[request.form["username"]]["id"]))
        return Response('''
          login success!<br />
          <a href="/protected/">protected</a><br />
          <a href="/logout/">logout</a>
          ''')
      else:
        return abort(401)
    else:
        return render_template("login.html")

    # ログアウトパス
    @app.route('/logout/')
    @login_required
    def logout():
        logout_user()
        return Response('''
        logout success!<br />
        <a href="/login/">login</a>
        ''')
    """
 ################

  # CORS対応
  CORS(app)



  # DB設定を読み込む
  app.config.from_object('config.Config')
  db.init_app(app)

  app.register_blueprint(user_router, url_prefix='/api')
  app.register_blueprint(karuta_router, url_prefix='/api')
  app.register_blueprint(user_score_router, url_prefix='/api')
  app.register_blueprint(reading_list_router, url_prefix='/api')
  app.register_blueprint(user_reading_router, url_prefix='/api')
  return app

app = create_app()
