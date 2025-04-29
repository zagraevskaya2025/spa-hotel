# Используем официальный Python-образ
FROM python:3.11-slim

# Указываем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем только файл зависимостей и устанавливаем их
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь проект внутрь контейнера
COPY . .

# Создаём папки для статики и медиа
RUN mkdir -p /app/staticfiles /app/media

# Выполняем команду для сбора статики
RUN python manage.py collectstatic --noinput

# Открываем порт 8000 для приложения
EXPOSE 8000

# Команда для запуска приложения с использованием Gunicorn
CMD ["gunicorn", "spa_hotel.wsgi:application", "--bind", "0.0.0.0:8000"]
