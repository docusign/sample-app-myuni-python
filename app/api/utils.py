from flask import jsonify

from app.ds_config import DsConfig


def process_error(err):
    """Special handling for consent_required"""
    body = err.body.decode('utf8')
    if "consent_required" in body:
        consent_scopes = ' '.join(DsConfig.permission_scopes())
        consent_url = f"{DsConfig.auth_server()}/oauth/auth?response_type=code&scope={consent_scopes}&client_id={DsConfig.client_id()}&redirect_uri={DsConfig.return_url()}"
        return jsonify({
            'reason': 'Unauthorized',
            'response': 'Permissions should be granted for current integration',
            'url': consent_url}), 401
    else:
        return jsonify({
            'reason': err.reason,
            'response': err.body.decode('utf8')
        }), 400
