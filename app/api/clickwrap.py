from docusign_esign import ApiException
from flask import Blueprint, jsonify, request, session
from flask_cors import cross_origin

from app.api.utils import process_error, check_token
from app.clickwrap import Clickwrap

clickwrap = Blueprint('clickwrap', __name__)

@clickwrap.route('/clickwraps/transcript', methods=['POST'])
@cross_origin()
@check_token
def transcript_clickwrap():
    """Create clickwrap for an unofficial transcript"""
    try:
        req_json = request.get_json(force=True)
    except TypeError:
        return jsonify(message='Invalid json input'), 400

    clickwrap_args = {
        'terms_name': req_json['terms-name'],
        'display_name': req_json['display-name']
    }

    try:
        clickwrap_ = Clickwrap.create(clickwrap_args, session)
    except ApiException as exc:
        return process_error(exc)
    return jsonify(clickwrap=clickwrap_)
