from django.core.exceptions import ValidationError


def validate_score(value):
    if not 1 <= value <= 5:
        raise ValidationError('%s is not a valid score' % value)
