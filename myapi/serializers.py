# pylint: disable=W0311
# почему-то ругается на пробелы, хотя ничего копи-пастом не делал
"""
Модуль содержит сериалайзеры для каждой из моделей встроенной SQLite
"""

from rest_framework import serializers
from megafonTestApp.models import Users, Events, Tariffs


class UsersSerializer(serializers.HyperlinkedModelSerializer):
	"""
	Сериалайзер для модели Users
	"""

	class Meta:
		model = Users
		fields = '__all__'


class EventsSerializer(serializers.HyperlinkedModelSerializer):
	"""
	Сериалайзер для модели Events
	"""

	class Meta:
		model = Events
		fields = '__all__'


class TariffsSerializer(serializers.HyperlinkedModelSerializer):
	"""
	Сериалайзер для модели Tariffs
	"""

	class Meta:
		model = Tariffs
		fields = '__all__'
