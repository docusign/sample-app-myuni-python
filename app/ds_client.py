import time

import docusign_esign

from app.const import TOKEN_REPLACEMENT_IN_SECONDS, TOKEN_EXPIRATION_IN_SECONDS
from app.ds_config import DsConfig


class DsClient:
    """Docusign Client class"""
    account_id = None
    api_client = None
    account = None
    expiresTimestamp = 0
    instance = None

    def __init__(self):
        DsClient.api_client = docusign_esign.ApiClient()

    @staticmethod
    def get_instance(host=None):
        if DsClient.instance is None:
            DsClient.instance = DsClient()
        DsClient.instance.check_token()
        DsClient.instance.set_host(host)
        return DsClient.instance

    def check_token(self):
        current_time = int(round(time.time()))
        if not DsClient.account \
                or ((current_time + TOKEN_REPLACEMENT_IN_SECONDS) > DsClient.expiresTimestamp):
            self.update_token()

    def update_token(self):
        client = self.api_client
        client.set_base_path(DsConfig.aud())
        client.request_jwt_user_token(DsConfig.client_id(),
                                      DsConfig.impersonated_user_guid(),
                                      DsConfig.aud(),
                                      DsConfig.private_key(),
                                      TOKEN_EXPIRATION_IN_SECONDS,
                                      scopes=DsConfig.permission_scopes())

        if DsClient.account is None:
            DsClient.account = self.get_account_info()

        DsClient.base_uri = DsClient.account['base_uri'] + '/restapi'
        DsClient.account_id = DsClient.account['account_id']
        client.host = DsClient.base_uri
        DsClient.expiresTimestamp = int(round(time.time())) + TOKEN_EXPIRATION_IN_SECONDS

    def set_host(self, host):
        if host:
            self.api_client.host = host
        else:
            self.api_client.host = DsClient.account['base_uri'] + '/restapi'

    def get_account_info(self):
        client = self.api_client
        client.host = DsConfig.auth_server()
        response = client.call_api(
            '/oauth/userinfo', 'GET', response_type='object'
        )

        if len(response) > 1 and 200 > response[1] > 300:
            raise Exception('can not get user info: %d'.format(response[1]))

        accounts = response[0]['accounts']
        target = DsConfig.target_account_id()

        if target is None or target == 'FALSE':
            # Look for default
            for acc in accounts:
                if acc['is_default']:
                    return acc

        # Look for specific account
        for acc in accounts:
            if acc['account_id'] == target:
                return acc

        raise Exception(f'\n\nUser does not have access to account {target}\n\n')
