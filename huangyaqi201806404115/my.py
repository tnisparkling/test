from flask import Flask,jsonify,request
from flask_jwt_extended import JWTManager,create_access_token,jwt_required
class User(object):
    def __init__(self,username,password):
        self.username=username
        self.password=password
app=Flask(__name__)
app.config['JWT_SECRET_KEY']='super_secret'
jwt=JWTManager(app)
user={}
@app.route('/signup',methods=['POST'])
def signup():
    if not request.is_json:
        return jsonify({"提示":"请求中缺少JSON"}),400
    username=request.json.get('username',None)
    password=request.json.get('password',None)
    if (not username) or (not password):
        return jsonify({"提示":"缺少用户名或密码"}),400
    if username in user:
        return jsonify({"提示":"用户名"}),401
    user[username]=User(username,password)
    return jsonify({"提示":"注册成功"}),200
@app.route('/login',methods=['POST'])
def login():
    if not request.is_json:
        return jsonify({"提示":"请求中缺少JSON"}),400
    username=request.json.get('username',None)
    password=request.json.get('password',None)
    if (not username) or (not password):
        return jsonify({"提示":"缺少用户名或密码"}),401
    loginuser=user.get(username,None)
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
@app.route('/talk',methods=['POST'])
@jwt_required
def talk():
    return ('hello,world')
if __name__ == '__main__':
    app.run(port=5001)