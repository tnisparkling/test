from flask import Flask,jsonify,request
from flask_jwt_extended import JWTManager,create_access_token,jwt_required
import huangyaqi201806404115.huangyaqi1 as huangyaqi1
import huangyaqi201806404115.huangyaqi2 as huangyaqi2
import huangyaqi201806404115.huangyaqi3 as huangyaqi3
app=Flask(__name__)
app.config['JWT_SECRET_KEY']='super_secret'
jwt=JWTManager(app)
user={}
app.register_blueprint(huangyaqi1.app1)
app.register_blueprint(huangyaqi2.app2)
app.register_blueprint(huangyaqi3.app3)
if __name__ == '__main__':
    app.run()