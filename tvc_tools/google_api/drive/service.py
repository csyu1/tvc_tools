from typing import TypedDict

from googleapiclient.discovery import build

from tvc_tools.google_api.core import GoogleAPIMixin


class Permission(TypedDict):
    type: str
    role: str
    emailAddress: str


class GoogleDriveAPIService(GoogleAPIMixin):
    SCOPES = ["https://www.googleapis.com/auth/drive"]

    def __init__(self):
        super().__init__()
        self.drive_service = build("drive", "v3", credentials=self.credentials)

    def copy_file(self, file_id: str, name: str):
        file = {"name": name}
        result = self.drive_service.files().copy(fileId=file_id, body=file).execute()
        return result

    def share_file(self, file_id: str, permission: list[Permission]):
        for perm in permission:
            user_permission = {
                "type": perm["type"],
                "role": perm["role"],
                "emailAddress": perm["emailAddress"],
            }
            self.drive_service.permissions().create(
                fileId=file_id, body=user_permission, fields="id"
            ).execute()
