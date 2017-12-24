from flask import request, jsonify
from app.models import *
from app.auth import auth

@auth.route('/apidemo', methods = ['GET', 'POST'])
def apidemo():
    '''返回一个json'''

    jsonrequest = dict(errorCode=1, errMsg='操作成功')
    return jsonify(jsonrequest)