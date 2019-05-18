from flask import Flask,jsonify,request
from flask_jwt_extended import JWTManager,create_access_token,jwt_required
class User(object):
    def __init__(self,username,password):
        self.username = username
        self.password = password
app = Flask(__name__)
app.config['JWT_SECRET_KEY'] ='super-secret'
jwt = JWTManager(app)
users = {}
# @app.route('/signup',methods=['POST'])
# def signup():
#     if not request.is_json:
#         return jsonify({"提示":"没有json"}),400
#     username = request.json.get('username',None)
#     password = request.json.get('password',None)
#     if not username:
#         return jsonify({"提示":"没有username"}),400
#     if not password:
#         return jsonify({"提示":"没有password"}),400
#     if username in users:
#         return jsonify({"提示":"username已经用过了"}),200
#     users[username]= User(username,password)
#     return jsonify({"提示":"注册成功"})
# @app.route('/login',methods = ['POST'])
# def login():
#     if not request.is_json:
#         return jsonify({"提示":"没有json"}),400
#     username = request.json.get('username',None)
#     password = request.json.get('password',None)
#     if (not username) or (not password):
#         return jsonify({"提示","没有username或者password"}),400
#     loginuser = users.get(username,None)
#     if not loginuser:
#         return jsonify({"提示":"用户不存在"}),401
#     elif loginuser and loginuser.password == password:
#         return jsonify(access_token=create_access_token(identity=username)),200
#     else:
#         return jsonify({"提示":"username和password不正确"}),401
@app.route('/talk',methods = ['POST'])
@jwt_required
def talk():
    if not request.is_json:
        return jsonify({"提示","参数不在json中！"})
    SenForm = request.json.get('sentence')
    return jsonify({'回复',"talker.talk(SenFrom)"})


import say.sayhi as sayhi
app.register_blueprint(sayhi.oop)
import say.text as text
app.register_blueprint(text.opq)

import say.sayhello as sayhello
app.register_blueprint(sayhello.you)



if __name__=='__main__':
    app.run()



