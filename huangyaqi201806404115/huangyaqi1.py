from flask import Blueprint,jsonify,request
class User(object):
    def __init__(self,username,password):
        self.username=username
        self.password=password
user={}
app1=Blueprint('app1',__name__)
@app1.route('/signup',methods=['POST'])
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