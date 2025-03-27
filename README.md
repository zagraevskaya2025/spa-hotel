# SPA-отель в Пятигорске

Веб-приложение для SPA-отеля, разработанное на Django. Сайт предоставляет информацию об услугах отеля, позволяет просматривать фотогалерею и оставлять отзывы.

🌐 **Сайт доступен по адресу:** [https://spa-hotel-3.onrender.com/](https://spa-hotel-3.onrender.com/)

## Основной функционал

- Просмотр информации об отеле и предоставляемых услугах
- Галерея с фотографиями отеля и описаниями
- Система отзывов с рейтингом (от 1 до 5 звезд)
- Страница контактов с интерактивной картой
- Административная панель для управления контентом
- Адаптивный дизайн для всех устройств

## Технологии

- Python 3.10
- Django 5.1
- SQLite
- Bootstrap 5
- Font Awesome
- Gunicorn (для production)

## Установка и запуск

1. Клонируйте репозиторий:
```bash
git clone [URL репозитория]
cd spa_hotel
```

2. Создайте виртуальное окружение:
```bash
python -m venv myenv
myenv\Scripts\activate  # для Windows
source myenv/bin/activate  # для Linux/Mac
```

3. Установите зависимости:
```bash
pip install -r requirements.txt
```

4. Выполните миграции:
```bash
python manage.py migrate
```

5. Создайте суперпользователя:
```bash
python manage.py createsuperuser
```

6. Запустите сервер:
```bash
python manage.py runserver
```

7. Откройте в браузере: http://127.0.0.1:8000

## Структура проекта

spa_hotel/

├── main/ # Основное приложение

│ ├── migrations/ # Миграции базы данных

│ ├── admin.py # Настройки админ-панели

│ ├── context_processors.py

│ ├── forms.py # Формы

│ ├── models.py # Модели данных

│ ├── urls.py # URL маршруты

│ └── views.py # Представления

├── spa_hotel/ # Настройки проекта

│ ├── settings.py # Основные настройки

│ ├── urls.py # Главные URL маршруты

│ └── wsgi.py # WSGI конфигурация

├── static/ # Статические файлы

│ ├── css/ # CSS стили

│ ├── uploads/ # Загруженные изображения

│ └── videos/ # Видеофайлы

├── templates/ # HTML шаблоны

│ ├── admin/ # Шаблоны админки

│ │ ├── panel.html

│ │ └── page_form.html

│ ├── registration/ # Шаблоны авторизации

│ │ └── logged_out.html

│ ├── base.html # Базовый шаблон

│ ├── contacts.html # Страница контактов

│ ├── feedback.html # Страница отзывов

│ ├── gallery.html # Галерея

│ ├── index.html # Главная страница

│ ├── login.html # Страница входа

│ ├── page_view.html # Шаблон для отображения страниц

│ └── services.html # Страница услуг

├── manage.py # Скрипт управления

├── requirements.txt # Зависимости проекта

└── README.md # Документация

