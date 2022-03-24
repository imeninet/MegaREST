# pylint: disable=W0311
# pylint: disable=R0901
"""
Модуль содержит представления для работы REST-сервиса
"""

from rest_framework import viewsets
from megafonTestApp.models import Users, Tariffs, Events
from .serializers import UsersSerializer, TariffsSerializer, EventsSerializer


class UsersViews(viewsets.ModelViewSet):
	"""
	Представления для обработки запросов к таблице Абоненты/Пользователи
	"""
	queryset = Users.objects.all()
	serializer_class = UsersSerializer


class TarifsViews(viewsets.ModelViewSet):
	"""
	Представления для обработки запросов к таблице Тарифы
	"""
	queryset = Tariffs.objects.all()
	serializer_class = TariffsSerializer


class EventsViews(viewsets.ModelViewSet):
	"""
	Представления для обработки запросов к таблице События
	"""
	queryset = Events.objects.all()
	serializer_class = EventsSerializer
