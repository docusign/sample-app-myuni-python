import os

from dotenv import load_dotenv


class DsConfig:
    instance = None
    config = {}

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = DsConfig()
        return cls.instance

    def __init__(self):
        client_id = os.environ.get('DS_CLIENT_ID', None)
        if client_id is None:
            load_dotenv()

        self.config['DS_AUTH_SERVER'] = os.environ.get('REACT_APP_DS_AUTH_SERVER')
        self.config['DS_RETURN_URL'] = os.environ.get('REACT_APP_DS_RETURN_URL')

        self.config['DS_CLIENT_ID'] = os.environ.get('DS_CLIENT_ID', None)
        self.config['DS_IMPERSONATED_USER_GUID'] = os.environ.get('DS_IMPERSONATED_USER_GUID')
        self.config['DS_TARGET_ACCOUNT_ID'] = os.environ.get('DS_TARGET_ACCOUNT_ID')
        self.config['DS_PRIVATE_KEY'] = os.environ.get('DS_PRIVATE_KEY')
        self.config['DS_PAYMENT_GATEWAY_ID'] = os.environ.get('DS_PAYMENT_GATEWAY_ID')
        self.config['DS_PAYMENT_GATEWAY_NAME'] = os.environ.get('DS_PAYMENT_GATEWAY_NAME')
        self.config['DS_PAYMENT_GATEWAY_DISPLAY_NAME'] = os.environ.get('DS_PAYMENT_GATEWAY_DISPLAY_NAME')
        if not self.config['DS_CLIENT_ID']:
            raise Exception(f'Missing config file |.env| and environment variables are not set.')

    @classmethod
    def auth_server(cls):
        return cls.get_instance().config['DS_AUTH_SERVER']

    @classmethod
    def client_id(cls):
        return cls.get_instance().config['DS_CLIENT_ID']

    @classmethod
    def impersonated_user_guid(cls):
        return cls.get_instance().config['DS_IMPERSONATED_USER_GUID']

    @classmethod
    def target_account_id(cls):
        return cls.get_instance().config['DS_TARGET_ACCOUNT_ID']

    @classmethod
    def private_key(cls):
        if os.path.isfile(cls.get_instance().config['DS_PRIVATE_KEY']):
            return bytes(open(cls.get_instance().config['DS_PRIVATE_KEY'], 'rb').read())
        else:
            return cls.get_instance().config['DS_PRIVATE_KEY']

    @classmethod
    def gateway_id(cls):
        return cls.get_instance().config['DS_PAYMENT_GATEWAY_ID']

    @classmethod
    def gateway_name(cls):
        return cls.get_instance().config['DS_PAYMENT_GATEWAY_NAME']

    @classmethod
    def gateway_display_name(cls):
        return cls.get_instance().config['DS_PAYMENT_GATEWAY_DISPLAY_NAME']

    @classmethod
    def return_url(cls):
        return cls.get_instance().config['DS_RETURN_URL']

    @classmethod
    def aud(cls):
        auth_server = cls.auth_server()
        if 'https://' in auth_server:
            aud = auth_server[8:]
        else:
            aud = auth_server[7:]
        return aud

    @classmethod
    def permission_scopes(cls):
        return ['signature', 'impersonation', 'click.manage']
