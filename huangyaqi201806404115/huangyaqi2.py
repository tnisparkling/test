from flask import Blueprint,jsonify,request
from flask_jwt_extended import JWTManager,create_access_token,jwt_required
import huangyaqi201806404115.huangyaqi1 as huangyaqi1
class User(object):
    def __init__(self,username,password):
        self.username=username
        self.password=password
user={}
app2=Blueprint('app2',__name__)
@app2.route('/login',methods=['POST'])
def login():
    if not request.is_json:
        return jsonify({"提示":"请求中缺少JSON"}),400
    username=request.json.get('username',None)
    password=request.json.get('password',None)
    if (not username) or (not password):
        return jsonify({"提示":"缺少用户名或密码"}),401
    loginuser=huangyaqi1.user.get(username,None)
    if not loginuser:
        return jsonify({"提示":"用户名不存在"}),401
    elif loginuser.password==password:
        return jsonify(access_token=create_access_token(identity=username)),200
    else:
        return jsonify({"提示":"密码错误"}),401
    if loginuser and login.password==password:

        return jsonify({"提示":"access_token=create_access_token(identity=username)"}),200
    else:
        return jsonify({"输出":"用户名或密码错误"}),401
