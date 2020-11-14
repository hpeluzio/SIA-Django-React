import datetime
from django.core.exceptions import ValidationError


def atual_year_not_past(year):
    if isinstance(year, int) and datetime.datetime.now().year <= year:
        return True
    raise ValidationError('Data não pode ser inferior ao ano atual.')
