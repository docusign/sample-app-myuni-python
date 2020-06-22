from docusign_esign import ApiException
from flask import request, jsonify
from app.api import authenticate, api
from app.envelope import Envelope


@api.route('/envelope/multi_signers', methods=['POST'])
@authenticate
def multi_signers():
    try:
        req_json = request.get_json(force=True)
        student = req_json['student']
        envelope_args = {
            "signer_client_id": 1000,
            "ds_return_url": req_json['callback-url'],
            "account_id": req_json['account-id'],
            "base_path": req_json['base-path'],
            'access_token': request.headers.get('Authorization').replace('Bearer ', '')
        }
    except TypeError:
        return jsonify(message="Invalid JSON input"), 400

    try:
        envelope = Envelope.create('multi-sign.html', student, envelope_args)
        envelope_id = Envelope.send(envelope, envelope_args)
        result = Envelope.get_view(envelope_id,  envelope_args, student)
    except ApiException as e:
        return jsonify({'error': e.body.decode('utf-8')}), 400
    return jsonify({"envelope_id": envelope_id, "redirect_url": result.url})


@api.route('/envelope/list', methods=['POST'])
@authenticate
def envelope_list():
    try:
        req_json = request.get_json(force=True)
        envelope_args = {
            'account_id': req_json['account-id'],
            'from_date': req_json['from-date'],
            "base_path": req_json['base-path'],
            'access_token': request.headers.get('Authorization').replace('Bearer ', '')
        }
    except TypeError:
        return jsonify(message="Invalid json input"), 400

    try:
        envelopes_information = Envelope.list(envelope_args)
    except ApiException as e:
        return jsonify({'error': e.body.decode('utf-8')}), 400

    return jsonify({"envelopes": envelopes_information.to_dict()})

