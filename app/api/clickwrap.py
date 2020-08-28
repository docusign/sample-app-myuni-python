from docusign_esign import ApiException
from flask import Blueprint, jsonify, request
from flask_cors import cross_origin

from app.api.utils import process_error, check_token
from app.clickwrap import Clickwrap

clickwrap = Blueprint('clickwrap', __name__)

@clickwrap.route('/clickwraps/transcript', methods=['POST'])
@cross_origin(supports_credentials=True)
@check_token
def transcript_clickwrap():
    """Create clickwrap for an unofficial transcript"""
    try:
        try:
            req_json = request.get_json(force=True)
            clickwrap_args = {
                'terms_name': req_json['terms-name'],
                'display_name': req_json['display-name'],
            }
        except TypeError:
            return jsonify(message='Invalid json input'), 400
        clickwrap = Clickwrap.create(clickwrap_args)
    except ApiException as ex:
        return process_error(ex)
    return jsonify(clickwrap=clickwrap)