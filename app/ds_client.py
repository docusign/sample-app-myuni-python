import time
import uuid

import docusign_esign

from app.const import TOKEN_EXPIRATION_IN_SECONDS
from app.ds_config import DsConfig


class DsClient:
    """Docusign Client class"""
    account_id = None
    api_client = None
    account = None
    expiresTimestamp = 0
    instance = None
    logged = False
    jwt_auth = False
    code_grant = False
    payment_gateway = None

    def __init__(self):
        DsClient.api_client = docusign_esign.ApiClient()

    @classmethod
    def get_instance(cls, host=None):
        if cls.instance is None:
            cls.instance = cls()
        cls.instance._set_host(host)
        return DsClient.instance

    @classmethod
    def update_token(cls):
        client = cls.get_instance(DsConfig.auth_server()).api_client
        client.set_base_path(DsConfig.aud())
        client.request_jwt_user_token(DsConfig.client_id(),
                                      DsConfig.impersonated_user_guid(),
                                      DsConfig.aud(),
                                      DsConfig.private_key(),
                                      TOKEN_EXPIRATION_IN_SECONDS,
                                      scopes=DsConfig.permission_scopes())

        if cls.account is None:
            cls.account = cls.instance._get_account_info()

        cls.base_uri = cls.account['base_uri'] + '/restapi'
        cls.account_id = cls.account['account_id']
        client.host = cls.base_uri
        cls.expiresTimestamp = int(round(time.time())) + TOKEN_EXPIRATION_IN_SECONDS
        cls.logged = True
        cls.jwt_auth = True

    def _set_host(self, host):
        if host:
            self.api_client.host = host
        else:
            self.api_client.host = DsClient.account['base_uri'] + '/restapi'

    def _get_account_info(self):
        client = self.api_client
        client.host = DsConfig.auth_server()
        response = client.call_api(
            '/oauth/userinfo', 'GET', response_type='object'
        )

        if len(response) > 1 and 300 > response[1] > 200:
            raise Exception('Cannot get user info: %d'.format(response[1]))

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

    @classmethod
    def code_auth(cls):
        client = cls.get_instance(DsConfig.auth_server()).api_client
        client.set_oauth_host_name(oauth_host_name=DsConfig.aud())
        state = uuid.uuid4().hex.upper()
        redirect_uri = DsConfig.return_url() + "/callback"

        uri = client.get_authorization_uri(
            client_id=DsConfig.client_id(),
            scopes=DsConfig.code_grant_scopes(),
            redirect_uri=redirect_uri,
            response_type="code",
            state=state
        )

        return uri

    @classmethod
    def callback(cls, code):
        """Callback method for obtaining access token"""
        client = cls.api_client
        response = client.generate_access_token(
            client_id=DsConfig.client_id(),
            client_secret=DsConfig.client_secret(),
            code=code
        )

        client.set_base_path(DsConfig.aud())
        client.set_default_header(header_name="Authorization", header_value=f"Bearer {response.access_token}")
        if cls.account is None:
            cls.account = cls.instance._get_account_info()

        cls.account_id = cls.account['account_id']
        cls.base_uri = cls.account['base_uri'] + '/restapi'
        client.host = cls.base_uri

        cls.expiresTimestamp = int(round(time.time())) + int(response.expires_in)
        cls.logged = True
        cls.code_grant = True

    @classmethod
    def destroy(cls):
        """Clear the session"""
        cls.account_id = None
        cls.api_client = None
        cls.account = None
        cls.expiresTimestamp = 0
        cls.instance = None
        cls.logged = False
        cls.code_grant = False
        cls.jwt_auth = False
        cls.payment_gateway = None
        DsConfig.instance = None

    @classmethod
    def check_payment_gateway(cls):
        if cls.payment_gateway:
            return True

        client = cls.api_client
        account_api = docusign_esign.AccountsApi(api_client=client)
        response = account_api.get_all_payment_gateway_accounts(account_id=cls.account_id)
        if response.payment_gateway_accounts:
            payment_gateways = [gateway for gateway in response.payment_gateway_accounts if
                                gateway.is_enabled == 'true']
            if payment_gateways:
                DsConfig.set_gateway_display_name(payment_gateways[0].display_name)
                DsConfig.set_gateway_name(payment_gateways[0].payment_gateway)
                DsConfig.set_gateway_id(payment_gateways[0].payment_gateway_account_id)
                cls.payment_gateway = payment_gateways[0]
                return True
        return False
