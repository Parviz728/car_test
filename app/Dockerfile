# Базовый образ контейнера
FROM python:3-alpine

# Рабочая директория
RUN mkdir /usr/local/app
WORKDIR /usr/local/app

# Открытые порты
# app
EXPOSE 5000

# Установка необходимых пакетов
COPY requirements.txt ./
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Копирование проекта
COPY ./ ./

# Запуск сервера
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0", "--port=5000"]
