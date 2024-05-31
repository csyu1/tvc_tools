#!/usr/bin/env python3
from tvc_tools.google_api.forms import GoogleFormsAPIService

if __name__ == "__main__":
    google_forms_service = GoogleFormsAPIService()
    form_id, form_url = google_forms_service.create_form(
        title="Test Form",
        document_title="This is a test form",
    )
    print(f"Form ID: {form_id}")
    print(f"Form URL: {form_url}")
