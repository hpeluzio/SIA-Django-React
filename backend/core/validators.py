import datetime
from django.core.exceptions import ValidationError


def atual_year_not_past(year):
    if isinstance(year, int) and datetime.datetime.now().year <= year:
        return True
    raise ValidationError('Data não pode ser inferior ao ano atual.')


def data_validate(year):
    if isinstance(year, int) and year >= 2010 and year <= 2999:
        return
    raise ValidationError('Data irregular.')


def min_value_date(year):
    if year >= 2010:
        return
    raise ValidationError('Data muito antiga.')


def max_value_date(year):
    if year <= 2999:
        return
    raise ValidationError('Data muito futura.')
