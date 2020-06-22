from docusign_esign import ApiException
from flask import Blueprint, jsonify, request, redirect, url_for
from flask_cors import cross_origin

from app.api.utils import process_error
from app.ds_client import DsClient

auth = Blueprint('auth', __name__)


@auth.route('/code_grant_auth', methods=['GET'])
@cross_origin(support_creadentials=True)
def code_grant_auth():
    try:
        url = DsClient.code_auth()
    except ApiException as ex:
        return process_error(ex)
    return jsonify({
        'reason': 'Unauthorized',
        'response': 'Permissions should be granted for current integration',
        'url': url}), 401


@auth.route('/callback', methods=['POST'])
@cross_origin(support_creadentials=True)
def callback():
    try:
        try:
            req_json = request.get_json(force=True)
            code = req_json['code']
        except TypeError:
            return jsonify(message='Invalid json input'), 400
        DsClient.callback(code)
    except ApiException:
        return redirect(url_for("auth.jwt_auth"), code=307)
    return jsonify(message="Logged in with code grant"), 200


@auth.route('/jwt_auth', methods=['POST'])
@cross_origin(support_creadentials=True)
def jwt_auth():
    try:
        DsClient.update_token()
    except ApiException as ex:
        return process_error(ex)
    return jsonify(message="Logged in with JWT"), 200


@auth.route('/get_status', methods=['GET'])
@cross_origin(support_creadentials=True)
def get_status():
    if DsClient.code_grant:
        return jsonify(logged=DsClient.logged, auth_type="code_grant"), 200
    elif DsClient.jwt_auth:
        return jsonify(logged=DsClient.logged, auth_type="jwt"), 200
    return jsonify(logged=DsClient.logged, auth_type="undefined"), 200


@auth.route('/logout', methods=['POST'])
@cross_origin(support_credentials=True)
def log_out():
    DsClient.destroy()
    return jsonify(message="Logged out"), 200


@auth.route('/check_payment', methods=['GET'])
@cross_origin(support_credentials=True)
def check_payment():
    try:
        if DsClient.check_payment_gateway():
            return jsonify(message="User has a payment gateway account"), 200
        else:
            return jsonify(message="User doesn't have a payment gateway account"), 402
    except ApiException as ex:
        return process_error(ex)
