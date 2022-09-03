from datetime import date

from django.core.exceptions import ValidationError


def validate_max_year(value):
    if value > date.today().year:
        raise ValidationError(message='Year must less or equal than current')
    return value
