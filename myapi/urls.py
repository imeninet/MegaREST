"""
Модуль содержит пути для реализации обращений REST по каждой таблице из задания на Stepik
"""
from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UsersViews)
router.register(r'tariffs', views.TarifsViews)
router.register(r'events', views.EventsViews)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]