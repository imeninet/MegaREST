"""
Модуль содержит подключения моделей Users, Tariffs и Events на админ-панель.
"""

from django.contrib import admin
from .models import Users, Tariffs, Events


admin.site.register(Users)
admin.site.register(Tariffs)
admin.site.register(Events)
