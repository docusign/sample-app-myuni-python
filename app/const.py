from os import path

TPL_PATH = path.abspath(
    path.join(path.dirname(path.realpath(__file__)), 'templates/')
)
IMG_PATH = path.abspath(
    path.join(path.dirname(path.realpath(__file__)), "images/")
)

TOKEN_EXPIRATION_IN_SECONDS = 3600
TOKEN_REPLACEMENT_IN_SECONDS = 10 * 60

CLICKWRAP_BASE_HOST = 'https://demo.docusign.net'
CLICKWRAP_BASE_URI = '/clickapi/v1/accounts'
CLICKWRAP_TIME_DELTA_IN_MINUTES = 15
