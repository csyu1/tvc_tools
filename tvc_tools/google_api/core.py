from google.oauth2 import service_account

from tvc_tools.core.settings import SERVICE_ACCOUNT_FILE

class GoogleAPIMixin:

    SCOPES = []

    def __init__(self):
        assert self.SCOPES, 'SCOPES must be defined in the subclass'
        self.credentials = self.authenticate_service_account()

    def authenticate_service_account(self):
        credentials = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE, scopes=self.SCOPES)
        return credentials
