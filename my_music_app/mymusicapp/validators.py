from django.core.exceptions import ValidationError


def validate_username_chars(value):
    for v in value:
        if v != '_' and not v.isalnum():
            raise ValidationError("Ensure this value contains only letters, numbers, and underscore.")
