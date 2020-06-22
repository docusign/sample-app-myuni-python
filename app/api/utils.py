import time
from functools import wraps

from flask import jsonify, redirect, url_for

from app.ds_config import DsConfig
from app.ds_client import DsClient
from app.const import TOKEN_REPLACEMENT_IN_SECONDS


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


def check_token(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        current_time = int(round(time.time()))
        if (current_time + TOKEN_REPLACEMENT_IN_SECONDS) > DsClient.expiresTimestamp:
            if DsClient.jwt_auth:
                DsClient.get_instance().update_token()
            elif DsClient.code_grant:
                return redirect(url_for("auth.code_grant_auth"))
        return func(*args, **kwargs)
    return wrapper
