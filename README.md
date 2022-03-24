                                                                                                                                       
# REST-сервис по задаче Мегафона 

<p>Задачи приложения:</p>
<ul>
<li> Обеспечить функционирование REST-запросов.</li>
</ul>
<p> Функционал:</p>
<ul>
<li> Получение списка всех таблиц со ссылками;</li>
<li> Возможность перехода к нужной таблице, получение списка всех строк;</li>
<li> Для каждой записи возможно добавление, изменение, удаление, чтение данных;</li>
</ul>
<br>

#### Бэкенд
Python 3.8 + Django 3.2 + DRF + SQLite<br>


#### Фронтенд
"Из коробки" DjangoRestFramework

#### API
Все пути доступны локально http://127.0.0.1:8000/ <br><br>

*Встроенная SQLite наполнена тестовыми данными из задачи Stepik для возможности юзать приложение сразу после старта


## Quickstart

Run the following commands:

    sudo apt-get install -y git python3 venv python3-pip
    python3 -m pip install --upgrade pip
    git clone https://github.com/imeninet/MegaREST.git
    cd MegaREST
    
    python -m venv venv
    .\venv\Scripts\activate.bat

    pip3 install -r requirements.txt

Run the app locally:

    python3 manage.py runserver
