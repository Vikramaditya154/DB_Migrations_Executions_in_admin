from django.contrib import admin

# Register your models here.
from app.models import *

admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(AccessRecord)
# python manage.py migrate
# python manage.py makemigrations
# python manage.py migrate

# python manage.py createsuperuser