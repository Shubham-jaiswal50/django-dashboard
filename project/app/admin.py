from django.contrib import admin
from .models import EmpDatabase,AdminDatabase

# Register your models here.
admin.site.register(EmpDatabase)
admin.site.register(AdminDatabase)
