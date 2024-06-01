from typing import Literal


def create_text_question_item(
    title: str, paragraph: bool = False, required: bool = True, location_index: int = 0
):
    return {
        "createItem": {
            "item": {
                "title": title,
                "questionItem": {
                    "question": {
                        "required": required,
                        "textQuestion": {"paragraph": paragraph},
                    }
                },
            },
            "location": {"index": location_index},
        }
    }


def create_choices_question_item(
    title: str,
    choice_type: Literal["RADIO", "DROP_DOWN"],
    options: list[str],
    required: bool = True,
    location_index: int = 0,
):
    return {
        "createItem": {
            "item": {
                "title": title,
                "questionItem": {
                    "question": {
                        "required": required,
                        "choiceQuestion": {
                            "type": choice_type,
                            "options": [{"value": option} for option in options],
                        },
                    }
                },
            },
            "location": {"index": location_index},
        }
    }
