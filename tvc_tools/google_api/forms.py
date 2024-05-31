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

    def update_form(self, form_id: str, requests: dict):
        # requests = [
        #     {
        #         "createItem": {
        #             "item": {
        #                 "title": "What is your favorite color?",
        #                 "questionItem": {
        #                     "question": {
        #                         "required": True,
        #                         "choiceQuestion": {
        #                             "type": "RADIO",
        #                             "options": [
        #                                 {"value": "Red"},
        #                                 {"value": "Blue"},
        #                                 {"value": "Green"},
        #                                 {"value": "Yellow"}
        #                             ]
        #                         }
        #                     }
        #                 }
        #             },
        #             "location": {
        #                 "index": 0
        #             }
        #         }
        #     },
        #     {
        #         "createItem": {
        #             "item": {
        #                 "title": "What is your name?",
        #                 "questionItem": {
        #                     "question": {
        #                         "required": True,
        #                         "textQuestion": {}
        #                     }
        #                 }
        #             },
        #             "location": {
        #                 "index": 1
        #             }
        #         }
        #     },
        #     {
        #         "createItem": {
        #             "item": {
        #                 "title": "Tell us about yourself.",
        #                 "questionItem": {
        #                     "question": {
        #                         "textQuestion": {}
        #                     }
        #                 }
        #             },
        #             "location": {
        #                 "index": 2
        #             }
        #         }
        #     },
        #     {
        #         "createItem": {
        #             "item": {
        #                 "title": "When is your birthday?",
        #                 "questionItem": {
        #                     "question": {
        #                         "required": True,
        #                         "dateQuestion": {}
        #                     }
        #                 }
        #             },
        #             "location": {
        #                 "index": 3
        #             }
        #         }
        #     },
        #     {
        #         "createItem": {
        #             "item": {
        #                 "title": "Rate your satisfaction with our service",
        #                 "questionItem": {
        #                     "question": {
        #                         "required": True,
        #                         "scaleQuestion": {
        #                             "low": 1,
        #                             "high": 5
        #                         }
        #                     }
        #                 }
        #             },
        #             "location": {
        #                 "index": 4
        #             }
        #         }
        #     }
        # ]

        # Batch update to add items
        self.forms_service.forms().batchUpdate(
            formId=form_id, body={"requests": requests}
        ).execute()
