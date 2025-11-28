from django.contrib import admin
from .models import LoginData  # <-- yaha change karo

admin.site.register(LoginData)
