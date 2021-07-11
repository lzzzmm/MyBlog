from django.contrib import admin

# Register your models here.
from mysource.models import My_Source, My_source_detail

admin.site.register(My_Source)
admin.site.register(My_source_detail)