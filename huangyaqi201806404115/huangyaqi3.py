from flask import Blueprint
app3=Blueprint('app3',__name__)

@app3.route('/talk',methods=['POST'])
#@jwt_required
def talk():
    return ('hello,world')