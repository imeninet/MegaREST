from django.apps import AppConfig


class MyapiConfig(AppConfig):
    """
    Объявление класса приложения
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myapi'
