"""
Модуль содержит описание моделей для реализации REST-сервиса
"""

from django.db import models


class Tariffs(models.Model):
	"""
	Класс, описывающий модель Тарифы. Содержит поля из таблицы Тарифы практического задания на Stepik
	"""

	id = models.IntegerField(primary_key=True, verbose_name='id')
	name = models.CharField(max_length=30, verbose_name='Название')
	start_data = models.DateField(verbose_name='Дата начала действия')
	end_data = models.DateField(verbose_name='Дата конца действия')
	minuts = models.IntegerField(verbose_name='Объем минут')
	sms = models.IntegerField(verbose_name='Объем смс')
	mb = models.IntegerField(verbose_name='Объем трафика, мегабайт')

	class Meta:
		"""
		Мета-класс для понятной обертки на панели администратора
		"""
		verbose_name_plural = 'Тарифы'
		verbose_name = 'Тариф'


class Users(models.Model):
	"""
	Класс, описывающий модель Абоненты/Пользователи.
	Содержит поля из таблицы Абоненты/Пользователи практического задания на Stepik
	"""
	verbose_name = 'Абоненты/Пользователи'

	id = models.IntegerField(primary_key=True, verbose_name='id')
	balance = models.DecimalField(verbose_name='Текущий баланс', decimal_places=2, max_digits=1000000)
	add_data = models.DateField(verbose_name='Дата добавления')
	age_user = models.IntegerField(verbose_name='Возраст')
	city_user = models.CharField(max_length=30, verbose_name='Город проживания')
	act_time = models.DateTimeField(verbose_name='Временная метка последней активности')
	tariff = models.IntegerField(verbose_name='Активный тариф')

	class Meta:
		"""
		Мета-класс для понятной обертки на панели администратора
		"""
		verbose_name_plural = 'Абоненты/Пользователи'
		verbose_name = 'Абонент/Пользователь'


class Events(models.Model):
	"""
	Класс, описывающий модель События.
	Содержит поля из таблицы События практического задания на Stepik
	"""
	verbose_name = 'События'

	TYPE_EVENT = [
		('coll', 'Звонок'),
		('sms', 'смс'),
		('internet', 'Трафик')
	]

	id = models.IntegerField(primary_key=True, verbose_name='id')
	time_point = models.DateTimeField(verbose_name='Метка времени')
	user_id = models.IntegerField(verbose_name='id абонента')
	type_event = models.CharField(
		max_length=10,
		choices=TYPE_EVENT,
		verbose_name='Тип услуги'
	)
	size_sale = models.IntegerField(verbose_name='Объем затраченных единиц')

	class Meta:
		"""
		Мета-класс для понятной обертки на панели администратора
		"""
		verbose_name_plural = 'События'
		verbose_name = 'Событие'
