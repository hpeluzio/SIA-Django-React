l = (
    {"django.db.models.fields.AutoField": "id"},
    {"django.db.models.fields.DateField": "created_at"},
    {"django.db.models.fields.DateField": "updated_at"},
    {"django.db.models.fields.IntegerField": "trabalho_id"},
    {"django.db.models.fields.CharField": "nome"},
    {"django.db.models.fields.CharField": "orientador"},
    {"django.db.models.fields.CharField": "modalidade"},
    {"django.db.models.fields.CharField": "area"},
    {"django.db.models.fields.related.ForeignKey": "departamento"},
    {"django.db.models.fields.related.ForeignKey": "ano"}
)

# print(l)
t = []
# for item in l:
#     # print(item.values())
#     t.append(item.values())

# print(t)

for item in l:
    for k, v in item.items():
        print(v)
