from typing import Any

from googleapiclient.discovery import build

from tvc_tools.google_api.core import GoogleAPIMixin


class GoogleFormsAPIService(GoogleAPIMixin):
    # Define the scopes required
    SCOPES = ["https://www.googleapis.com/auth/forms.body"]

    def __init__(self):
        super().__init__()
        self.forms_service = build("forms", "v1", credentials=self.credentials)

    def create_form(self, title: str, document_title: str):
        form = form = {
            "info": {
                "title": title,
                "documentTitle": document_title,
            },
        }

        result = self.forms_service.forms().create(body=form).execute()
        form_id = result["formId"]
        form_url = result["responderUri"]

        return form_id, form_url

    def update_form(self, form_id: str, requests: list[dict[Any, Any]]):
        # Batch update to add items
        self.forms_service.forms().batchUpdate(
            formId=form_id, body={"requests": requests}
        ).execute()
