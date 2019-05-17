from flask import Flask, jsonify, request
class User(object):
    def __init__(self,username,passward):
        self.username = username
        self.password = passward
app = Flask(__name__)
users = {}
@app.route('/signup',methods=['POST'])
def signup():
    # if not request.is_json:
    #     return jsonify({"msg":"Missing JSON in request"}),400
    # username = request.args.get('username',None)
    # password = request.args.get('password',None)
    username=request.form['username']
    password=request.form['password']
    if not username:
        return jsonify({"msg":"Missing username parameter"}),400

    if not password:
        return jsonify({"msg":"Missing password parameter"}),400
    if username in users:
        return jsonify({"msg":"This username have used!"}),201
    users[username]=User(username,password)
    return jsonify({"msg":"signup success!"}),200









if __name__=='__main__':
    app.run()
