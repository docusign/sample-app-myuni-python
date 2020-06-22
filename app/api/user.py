import requests
from docusign_esign import ApiException
from flask import request, jsonify
from app.ds_config import DS_CONFIG
from app.api import api, authenticate

@api.route('/user/info', methods=['POST'])
@authenticate
def user_info():
    url = DS_CONFIG["authorization_server"] + "/oauth/userinfo"
    auth = {"Authorization": request.headers.get('Authorization')}
    try:
        response = requests.get(url, headers=auth).json()
    except ApiException as e:
        return jsonify({'error': e.body.decode('utf-8')}), 400
    return jsonify(response)