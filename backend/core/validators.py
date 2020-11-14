import datetime
from django.core.exceptions import ValidationError


def atual_year_not_past(year):
    print('entrou aqui')
    if isinstance(year, int) and datetime.datetime.now().year <= year:
        print('entrou aqui 2')
        return True
    print('entrou aqui 3')
    raise ValidationError('Data não pode ser inferior ao ano atual.')
