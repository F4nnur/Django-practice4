from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Test)
admin.site.register(Question)
admin.site.register(Entering)
